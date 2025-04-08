import os
import pandas as pd
from PyPDF2 import PdfReader
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
    return docs