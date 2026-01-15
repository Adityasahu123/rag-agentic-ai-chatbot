from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# 1. Read the PDF
loader = PyPDFLoader("data/agentic_ai.pdf")
pages = loader.load()

# 2. Split text into small chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(pages)

# 3. FREE embeddings (no money)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Store in FAISS vector database
db = FAISS.from_documents(chunks, embeddings)
db.save_local("vector_db")

print("Book stored successfully using FREE embeddings!")
