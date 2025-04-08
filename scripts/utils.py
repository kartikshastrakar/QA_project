import os
import pandas as pd
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.schema import Document

def load_documents(data_path):
    docs = []
    for file in os.listdir(data_path):
        file_path = os.path.join(data_path, file)
        if file.endswith(".pdf"):
            reader = PdfReader(file_path)
            text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
            docs.append(Document(page_content=text, metadata={"source": file}))
        elif file.endswith(".csv"):
            df = pd.read_csv(file_path)
            text = df.to_string()
            docs.append(Document(page_content=text, metadata={"source": file}))
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    return chunks

def embed_and_store(documents, index_folder):
    embeddings = OllamaEmbeddings(model="mistral")
    db = FAISS.from_documents(documents, embeddings)
    db.save_local(index_folder)

def retrieve_context(query, index_folder):
    embeddings = OllamaEmbeddings(model="mistral")
    db = FAISS.load_local(index_folder, embeddings, allow_dangerous_deserialization=True)
    results = db.similarity_search(query, k=5)
    return "\n".join([doc.page_content for doc in results])

def get_ollama_llm_response(query, context):
    llm = Ollama(model="mistral")
    prompt = (
        "Answer the question using ONLY the context below. "
        "If the answer is not there, say you don't know.\n\n"
        f"Context:\n{context}\n\nQuestion: {query}"
    )
    return llm.invoke(prompt)
