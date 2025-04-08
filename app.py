import os
import streamlit as st
from src.document_processing.loaders import load_documents
from src.document_processing.splitters import split_documents
from src.embeddings.faiss_store import embed_and_store, retrieve_context
from src.llm.ollama_integration import get_ollama_llm_response

# Define paths
DATA_FOLDER = "data"
INDEX_FOLDER = "vector_index"

# Ensure the index folder exists
os.makedirs(INDEX_FOLDER, exist_ok=True)

# Streamlit app
st.title("📄 PDF/CSV QA System")
st.write("Upload your PDF/CSV files, and ask questions about their content!")

# File uploader
uploaded_files = st.file_uploader("Upload PDF/CSV files", type=["pdf", "csv"], accept_multiple_files=True)

if uploaded_files:
    # Save uploaded files to the data folder
    for uploaded_file in uploaded_files:
        with open(os.path.join(DATA_FOLDER, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success("Files uploaded successfully!")

    # Process documents
    st.write("📂 Loading and processing documents...")
    documents = load_documents(DATA_FOLDER)
    chunks = split_documents(documents)

    # Embed and store
    st.write("🧠 Generating embeddings and storing in vector DB...")
    embed_and_store(chunks, INDEX_FOLDER)
    st.success("Documents processed and stored successfully!")

    # Question input
    st.write("🤖 Ask questions about your uploaded data:")
    user_query = st.text_input("Enter your question:")

    if user_query:
        # Retrieve context and generate response
        st.write("⏳ Retrieving context and generating answer...")
        context = retrieve_context(user_query, INDEX_FOLDER)
        answer = get_ollama_llm_response(user_query, context)

        # Display the answer
        st.write("✅ **Answer:**")
        st.write(answer)