import os
import sys
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.document_processing.loaders import load_documents
from src.document_processing.splitters import split_documents
from src.embeddings.faiss_store import embed_and_store, retrieve_context
from src.llm.ollama_integration import get_ollama_llm_response
from langchain.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def retrieve_context(query, index_folder, model="mistral", k=5):
    """
    Retrieve the most relevant context for a given query from the vector database.

    Args:
        query (str): The user's question.
        index_folder (str): Path to the folder containing the FAISS index.
        model (str): The embedding model to use.
        k (int): Number of top results to retrieve.

    Returns:
        str: The retrieved context or a message indicating no relevant context was found.
    """
    embeddings = OllamaEmbeddings(model=model)
    db = FAISS.load_local(index_folder, embeddings, allow_dangerous_deserialization=True)

    results = db.similarity_search(query, k=k)
    if not results:
        return "No relevant context found in the provided documents."
    return "\n".join([doc.page_content for doc in results])

def main():
    logging.info("Starting the PDF/CSV QA System...")
    data_folder = "data"
    index_folder = "vector_index"
    os.makedirs(index_folder, exist_ok=True)

    logging.info("Loading and processing documents...")
    documents = load_documents(data_folder)
    chunks = split_documents(documents)

    logging.info("Generating embeddings and storing in vector DB...")
    embed_and_store(chunks, index_folder)

    logging.info("System is ready for questions.")
    print("\n🤖 Ask questions about your PDF/CSV data (type 'exit' to quit):")
    while True:
        user_query = input("\n🔎 Question: ")
        if user_query.lower() == "exit":
            logging.info("Exiting the system.")
            break

        logging.info(f"Processing query: {user_query}")
        print("⏳ Retrieving context and generating answer...")
        context = retrieve_context(user_query, index_folder)
        answer = get_ollama_llm_response(user_query, context)

        print(f"\n✅ Answer:\n{answer}\n")

if __name__ == "__main__":
    main()
