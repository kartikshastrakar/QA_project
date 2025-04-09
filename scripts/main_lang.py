import os
import sys
import logging
from graphviz import Digraph  # For visualization

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.document_processing.loaders import load_documents
from src.document_processing.splitters import split_documents
from src.embeddings.faiss_store import embed_and_store, retrieve_context
from src.llm.ollama_integration import get_ollama_llm_response
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def retrieve_context(query, index_folder, model="mistral", k=5):
    embeddings = OllamaEmbeddings(model=model)
    db = FAISS.load_local(index_folder, embeddings, allow_dangerous_deserialization=True)
    results = db.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in results]) if results else "No relevant context found."

def visualize_workflow():
    """
    Visualizes the workflow of the PDF/CSV QA system using Graphviz.
    """
    dot = Digraph(comment="PDF/CSV QA Workflow")
    dot.node("A", "Load Documents")
    dot.node("B", "Split Documents")
    dot.node("C", "Generate Embeddings")
    dot.node("D", "Store in Vector DB")
    dot.node("E", "Retrieve Context")
    dot.node("F", "Generate Answer")
    dot.node("G", "User Interaction")

    dot.edges(["GA", "AB", "BC", "CD", "DE", "EF", "FG"])
    dot.render("workflow", format="png", cleanup=True)
    print("Workflow visualization saved as 'workflow.png'.")

def main():
    logging.info("Starting the PDF/CSV QA System...")
    data_folder = os.path.join(os.path.dirname(__file__), "..", "data")
    index_folder = os.path.join(os.path.dirname(__file__), "..", "vector_index")
    os.makedirs(index_folder, exist_ok=True)

    # Check if the data folder exists
    if not os.path.exists(data_folder):
        raise FileNotFoundError(f"The data folder '{data_folder}' does not exist. Please create it and add your files.")

    # Visualize the workflow
    visualize_workflow()

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