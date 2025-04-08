import os
from src.embeddings.faiss_store import embed_and_store, retrieve_context
from langchain.schema import Document

def test_faiss_store(tmp_path):
    index_folder = tmp_path / "index"
    docs = [Document(page_content="This is a test document.")]
    embed_and_store(docs, index_folder)

    query = "test"
    context = retrieve_context(query, index_folder)
    assert "test document" in context