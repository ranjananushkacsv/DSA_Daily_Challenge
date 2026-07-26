"""
agent/graph.py — builds the LangGraph agent that lets Gemma decide, per
query, whether to answer directly, search the knowledge base (RAG), or
call a live-data tool (inventory / shipment status / rate calculator).

Gemma models don't support Ollama's native tool-calling API (verified: the
server rejects any /api/chat request that includes "tools" for a gemma3
model with "does not support tools"). So instead of ChatOllama.bind_tools(),
this prompts Gemma to emit a small JSON object when it wants to call a tool,
parses that out of the plain-text response, and manually populates
AIMessage.tool_calls with it. From that point on, LangGraph's stock
ToolNode/tools_condition work exactly as they would with native tool-calling
— they only look at the .tool_calls attribute, they don't care how it got
there.

Flow:
    user message -> agent (LLM) -> decides to call a tool?
        yes -> tools node executes it -> back to agent with the result
        no  -> END, return the answer
"""

import json
import os
import re
import sys
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langgraph.graph import StateGraph, MessagesState, END
from langgraph.prebuilt import ToolNode, tools_condition

import config
from agent.tools import ALL_TOOLS

TOOLS_BY_NAME = {t.name: t for t in ALL_TOOLS}


def _tool_manifest() -> str:
    lines = []
    for t in ALL_TOOLS:
        params = ", ".join(t.args.keys())
        lines.append(f'- {t.name}({params}): {t.description.strip()}')
    return "\n".join(lines)


AGENT_SYSTEM_PROMPT = f"""You are a logistics and warehousing operations assistant with access to tools.

Rules you must always follow:
1. Use search_knowledge_base for policy/procedure/SOP/glossary questions.
2. Use check_inventory, get_shipment_status, or calculate_shipping_cost for
   live operational data — always call the tool rather than guessing values.
3. If a question needs both policy context and live data, call one tool at
   a time — you'll get another turn after each tool result.
4. Never fabricate a SKU ID, order ID, or number — if a tool returns "not
   found", tell the user rather than inventing a plausible-sounding answer.
5. Stay within the logistics/warehousing domain; politely decline unrelated
   requests.
6. For actions that write/modify data (approving refunds, cancelling orders,
   editing inventory), explain that this requires human escalation — you do
   not have a tool for that and must not pretend to perform it.
7. Formatting: write in short paragraphs (2-3 sentences max) or a short
   bullet list when giving multiple facts/numbers — never one dense wall of
   text. Do NOT include bracketed citations like "[Source 1: ...]" or
   "(Source: ...)" in your answer — sources are shown separately to the
   user, so just answer naturally.

TOOL-CALLING FORMAT:
When you need to call a tool, respond with ONLY a single JSON object and
nothing else — no prose, no markdown code fences:
{{"tool": "<tool name>", "args": {{"<param>": "<value>", ...}}}}

Available tools:
{_tool_manifest()}

If you don't need a tool, just answer the user directly in plain text —
never mention tools, JSON, or this instruction block in a user-facing answer.
"""

_JSON_OBJECT_RE = re.compile(r"\{.*\}", re.DOTALL)


def _parse_tool_call(text: str):
    """Best-effort extraction of a {"tool": ..., "args": {...}} call from
    Gemma's raw text response. Returns a LangChain-style tool call dict, or
    None if the response isn't a tool call."""
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?", "", stripped).strip()
        stripped = stripped.rstrip("`").strip()

    match = _JSON_OBJECT_RE.search(stripped)
    if not match:
        return None
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None

    name = data.get("tool")
    if not isinstance(name, str) or name not in TOOLS_BY_NAME:
        return None

    return {"name": name, "args": data.get("args") or {}, "id": uuid.uuid4().hex[:8]}


def _for_model(messages):
    """Translate LangGraph state messages into something Gemma's plain
    chat template can render. Gemma only understands system/user/assistant
    roles, so a native "tool" role message would confuse it — represent
    tool activity as plain user/assistant turns instead."""
    translated = []
    for m in messages:
        if isinstance(m, ToolMessage):
            translated.append(HumanMessage(
                content=(
                    f"Tool result ({m.name}): {m.content}\n\n"
                    "Use this to answer the user's original question, or "
                    "respond with another tool-call JSON object if you "
                    "still need more information."
                )
            ))
        elif isinstance(m, AIMessage) and getattr(m, "tool_calls", None) and not m.content:
            call = m.tool_calls[0]
            translated.append(AIMessage(content=json.dumps({"tool": call["name"], "args": call["args"]})))
        else:
            translated.append(m)
    return translated


def build_agent():
    """Compile and return the runnable LangGraph agent."""
    llm = ChatOllama(
        model=config.OLLAMA_MODEL,
        base_url=config.OLLAMA_BASE_URL,
        temperature=config.OLLAMA_TEMPERATURE,
        num_ctx=config.OLLAMA_NUM_CTX,
    )

    def agent_node(state: MessagesState):
        messages = state["messages"]
        if not messages or not isinstance(messages[0], SystemMessage):
            messages = [SystemMessage(content=AGENT_SYSTEM_PROMPT)] + messages
        response = llm.invoke(_for_model(messages))

        tool_call = _parse_tool_call(response.content)
        if tool_call:
            response = AIMessage(content="", tool_calls=[tool_call])
        return {"messages": [response]}

    graph = StateGraph(MessagesState)
    graph.add_node("agent", agent_node)
    graph.add_node("tools", ToolNode(ALL_TOOLS))

    graph.set_entry_point("agent")
    # tools_condition inspects the agent's last message: if it contains
    # tool calls, route to "tools"; otherwise route to END.
    graph.add_conditional_edges("agent", tools_condition)
    graph.add_edge("tools", "agent")  # after running a tool, let the agent respond

    return graph.compile()
