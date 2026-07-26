import streamlit as st
from langchain_community.llms import Ollama

# Set the title of the Streamlit app
st.title("🗣️ Qwen3-4B Local Chat")
st.caption("A simple chat interface powered by your locally-running Qwen3-4B model.")

# Initialize the Ollama model
llm = Ollama(model="qwen3:4b")

# Initialize chat history in Streamlit's session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What do you want to talk about?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get a response from the LLM
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # This is where the magic happens! We'll call the local LLM.
            # For a simple chat, we just pass the prompt directly.
            response = llm.invoke(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
