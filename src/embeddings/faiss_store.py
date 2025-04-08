from langchain_community.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings

def embed_and_store(documents, index_folder, model="mistral"):
    embeddings = OllamaEmbeddings(model=model)
    db = FAISS.from_documents(documents, embeddings)
    db.save_local(index_folder)

def retrieve_context(query, index_folder, model="mistral", k=5):
    embeddings = OllamaEmbeddings(model=model)
    db = FAISS.load_local(index_folder, embeddings, allow_dangerous_deserialization=True)
    results = db.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in results])