import os
import pytest
from src.document_processing.loaders import load_documents
from langchain.schema import Document

@pytest.fixture
def setup_test_data(tmp_path):
    # Create temporary test files
    pdf_file = tmp_path / "test.pdf"
    pdf_file.write_text("This is a test PDF.")

    csv_file = tmp_path / "test.csv"
    csv_file.write_text("col1,col2\nval1,val2")

    return tmp_path

def test_load_documents(setup_test_data):
    docs = load_documents(setup_test_data)
    assert len(docs) == 2
    assert all(isinstance(doc, Document) for doc in docs)