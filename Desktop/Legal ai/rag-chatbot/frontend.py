import streamlit as st
import os

# You'll need to make sure the vector store is built before running this app.
from rag_pipeline import answer_query, retrive_docs, llm_model

st.set_page_config(
    page_title="AI Legal Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a more polished look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background-color: #f0f2f6; /* Light gray background */
    }

    .css-1d391kg, .css-1y4p8bb { /* Streamlit container classes for main content */
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 4px #388E3C;
    }

    .stButton>button:hover {
        background-color: #45a049;
        box-shadow: 0 2px #388E3C;
        transform: translateY(2px);
    }

    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 2px solid #ddd;
        padding: 10px;
    }
    
    .stTextArea>div>div>textarea {
        border-radius: 8px;
        border: 2px solid #ddd;
        padding: 10px;
    }
    
    /* Custom chat message colors */
    [data-testid="stChatMessage"][role="user"] {
        background-color: #e3f2fd;
        border-radius: 10px;
        padding: 1rem;
    }

    [data-testid="stChatMessage"][role="AI Lawyer"] {
        background-color: #f1f8e9;
        border-radius: 10px;
        padding: 1rem;
    }

    h1, h2, h3 {
        color: #1f77b4;
    }

</style>
""", unsafe_allow_html=True)

# Use markdown and columns for a more visually appealing layout
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>AI Legal Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Your trusted assistant for legal document queries.</p>", unsafe_allow_html=True)

# Create two columns for a cleaner layout
col1, col2 = st.columns([1, 2])

with col1:
    # PDF Upload section with a clear title
    st.subheader("1. Upload a Legal Document")
    uploaded_file = st.file_uploader(
        "Upload PDF",
        type="pdf",
        accept_multiple_files=False,
        help="Please upload a PDF document to begin."
    )

    # Basic instructions
    st.info("After uploading the document, you can ask questions about its content.")

with col2:
    # Chatbot section
    st.subheader("2. Chat with the AI Lawyer")
    
    # Use session state to store chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Text area for user input with a clear label
    user_query = st.text_area(
        "Enter your query:",
        height=100,
        placeholder="e.g., 'What are the grounds for divorce?'",
        label_visibility="collapsed"
    )

    # Use Streamlit's button with a key for better control
    ask_question = st.button("Ask AI Lawyer")

    # --- RAG pipeline logic ---
    if ask_question:
        if uploaded_file is None:
            st.error("Please upload a valid file first.")
        elif user_query.strip() == "":
            st.warning("Please enter a query.")
        else:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.write(user_query)

            # Retrieve and answer
            try:
                retrived_docs = retrive_docs(user_query)
                response = answer_query(documents=retrived_docs, model=llm_model, query=user_query)
                
                # Add AI response to chat history
                st.session_state.messages.append({"role": "AI Lawyer", "content": response})
                with st.chat_message("AI Lawyer"):
                    st.write(response)
            
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.error("Please ensure your RAG pipeline and vector database are set up correctly.")
