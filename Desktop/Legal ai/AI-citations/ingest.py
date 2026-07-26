import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Try using FastEmbed instead of HuggingFace
try:
    from langchain_community.embeddings import FastEmbedEmbeddings
    embedding_model = FastEmbedEmbeddings()
except:
    # Fallback to simpler approach
    from langchain_community.embeddings import OllamaEmbeddings
    embedding_model = OllamaEmbeddings(model="nomic-embed-text")

# --- Step 1: Load Legal Documents ---
documents = []
for file in os.listdir("legal_docs"):
    if file.endswith(".pdf"):
        pdf_path = os.path.join("legal_docs", file)
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())

# --- Step 2: Split Documents into Chunks ---
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
chunks = text_splitter.split_documents(documents)

print(f"Loaded {len(documents)} documents and split into {len(chunks)} chunks.")

# --- Step 3: Create Embeddings and Store in Vector Database ---
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./legal_vector_db_free"
)

vector_db.persist()
print("Vector database created and saved to disk.")