from src.document_processing.splitters import split_documents
from langchain.schema import Document

def test_split_documents():
    docs = [Document(page_content="This is a test document." * 100)]
    chunks = split_documents(docs, chunk_size=50, chunk_overlap=10)
    assert len(chunks) > 1
    assert all(len(chunk.page_content) <= 50 for chunk in chunks)