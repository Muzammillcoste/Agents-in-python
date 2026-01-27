from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv


load_dotenv()


# Load PDF document
file_path = Path(__file__).parent / "nodejs.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

# Split document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = text_splitter.split_documents(documents=docs)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001")

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name='learning'
)


