from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load FREE embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector DB (trusted local file)
db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

def ask_question(question: str):
    docs = db.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    if not context.strip():
        answer = "I don't know."
        confidence = 0.0
    else:
        answer = context[:500]
        confidence = 0.9

    return {
        "answer": answer,
        "context": context,
        "confidence": confidence
    }
