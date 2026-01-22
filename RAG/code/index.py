from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


file_path = Path(__file__).parent / "nodejs.pdf"

loader = PyPDFLoader(file_path)
docs = loader.load()
print(docs[12]) 

