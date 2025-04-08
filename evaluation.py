from src.document_processing.loaders import load_documents
from src.document_processing.splitters import split_documents
from src.embeddings.faiss_store import embed_and_store, retrieve_context
from src.llm.ollama_integration import get_ollama_llm_response

def evaluate_pipeline(data_path, index_folder, test_query):
    """
    Evaluates the document processing and LLM pipeline.

    Args:
        data_path (str): Path to the folder containing documents (PDFs/CSVs).
        index_folder (str): Path to store the FAISS index.
        test_query (str): A sample query to test the pipeline.

    Returns:
        str: The response from the LLM based on the retrieved context.
    """
    print("Loading documents...")
    docs = load_documents(data_path)

    print("Splitting documents into chunks...")
    chunks = split_documents(docs)

    print("Embedding and storing documents...")
    embed_and_store(chunks, index_folder)

    print("Retrieving context for the query...")
    context = retrieve_context(test_query, index_folder)

    print("Generating response using the LLM...")
    response = get_ollama_llm_response(test_query, context)

    return response


if __name__ == "__main__":
    # Define paths and test query
    data_path = "data/"  # Path to your data folder
    index_folder = "index/"  # Path to store FAISS index
    test_query = "What is the content of the sales report?"

    # Run the evaluation
    print("Starting pipeline evaluation...")
    response = evaluate_pipeline(data_path, index_folder, test_query)
    print("\nLLM Response:")
    print(response)