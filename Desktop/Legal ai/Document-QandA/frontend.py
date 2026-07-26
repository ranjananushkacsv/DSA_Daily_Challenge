import streamlit as st
import os
import tempfile
from pathlib import Path

# Import your existing RAG pipeline functions
from rag_pipeline import answer_query, llm_model

# Import vector database functions for dynamic processing
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

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
        background-color: #f0f2f6;
    }

    .css-1d391kg, .css-1y4p8bb {
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

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None
if "current_file_name" not in st.session_state:
    st.session_state.current_file_name = None

# Functions for dynamic PDF processing
@st.cache_resource
def get_embeddings_model():
    """Initialize and cache the embeddings model"""
    try:
        embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b")
        return embeddings
    except Exception as e:
        st.error(f"Error initializing embeddings model: {e}")
        return None

def process_uploaded_pdf(uploaded_file):
    """Process uploaded PDF and create vector database"""
    try:
        # Create a temporary file to save the uploaded PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name
        
        # Load the PDF
        loader = PDFPlumberLoader(temp_file_path)
        documents = loader.load()
        
        if not documents:
            st.error("No content found in the uploaded PDF.")
            return None
        
        # Create text chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True
        )
        text_chunks = text_splitter.split_documents(documents)
        
        # Get embeddings model
        embeddings = get_embeddings_model()
        if not embeddings:
            return None
        
        # Create vector database
        vector_db = FAISS.from_documents(text_chunks, embeddings)
        
        # Clean up temporary file
        os.unlink(temp_file_path)
        
        return vector_db, len(documents), len(text_chunks)
        
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        return None

def retrieve_docs_from_db(query, vector_db):
    """Retrieve documents from the provided vector database"""
    if vector_db is None:
        return []
    return vector_db.similarity_search(query)

def get_context_from_docs(documents):
    """Get context from retrieved documents"""
    context = "\n\n".join([doc.page_content for doc in documents])
    return context

# Header
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>AI Legal Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Upload your legal document and ask questions about its content.</p>", unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("1. Upload a Legal Document")
    uploaded_file = st.file_uploader(
        "Upload PDF",
        type="pdf",
        accept_multiple_files=False,
        help="Upload a PDF document to analyze its content."
    )
    
    # Process uploaded file
    if uploaded_file is not None:
        file_name = uploaded_file.name
        
        # Check if this is a new file
        if st.session_state.current_file_name != file_name:
            st.session_state.current_file_name = file_name
            
            with st.spinner("Processing your document... This may take a moment."):
                result = process_uploaded_pdf(uploaded_file)
                
                if result:
                    vector_db, num_pages, num_chunks = result
                    st.session_state.vector_db = vector_db
                    
                    st.success(f"✅ Document processed successfully!")
                    st.info(f"📄 Pages: {num_pages} | 📝 Text chunks: {num_chunks}")
                    
                    # Clear previous messages when new file is uploaded
                    st.session_state.messages = []
                else:
                    st.error("❌ Failed to process the document. Please try again.")
        else:
            st.success(f"✅ Document '{file_name}' is ready for questions!")
    
    # Instructions
    if uploaded_file is None:
        st.info("👆 Please upload a PDF document to get started.")
    else:
        st.success("🎉 Document loaded! You can now ask questions in the chat.")

with col2:
    st.subheader("2. Chat with the AI Lawyer")
    
    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    user_query = st.chat_input("Ask a question about your document...")
    
    # Process user query
    if user_query:
        if uploaded_file is None:
            st.error("Please upload a PDF file first.")
        elif st.session_state.vector_db is None:
            st.error("Document is still being processed. Please wait.")
        else:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.write(user_query)

            # Generate response
            try:
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        # Retrieve relevant documents
                        retrieved_docs = retrieve_docs_from_db(user_query, st.session_state.vector_db)
                        
                        if not retrieved_docs:
                            response = "I couldn't find relevant information in the document to answer your question. Please try rephrasing or ask about different content."
                        else:
                            # Generate answer using your existing function
                            response = answer_query(
                                documents=retrieved_docs, 
                                model=llm_model, 
                                query=user_query
                            )
                        
                        st.write(response)
                        
                        # Add AI response to chat history
                        st.session_state.messages.append({"role": "assistant", "content": response})
            
            except Exception as e:
                st.error(f"An error occurred while generating the response: {e}")
                st.error("Please ensure your models are running correctly.")

# Sidebar with information
with st.sidebar:
    
    st.header("System Status")
    if uploaded_file:
        st.success("✅ Document loaded")
        if st.session_state.vector_db:
            st.success("Ready to answer questions")
        else:
            st.warning("⏳ Processing document...")
    else:
        st.info("⏳ Waiting for document upload")
    
    st.header("🔧 Features")
    st.markdown("""
    - **Dynamic PDF processing**
    - **Semantic search**
    - **Context-aware responses**
    - **Chat history**
    - **Error handling**
    """)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>AI Legal Assistant - Powered by RAG Technology</p>", unsafe_allow_html=True)