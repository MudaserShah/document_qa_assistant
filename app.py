from fastapi import FastAPI

from src.components.loader import LoadPDF
from src.components.splitter import Splitter
from src.components.embeddings import EmbeddingModel
from src.components.vectorstore import QdrantDB

from src.pipeline.rag_pipeline import RAGPipeline

from src.config import PDF_PATH

from src.schema import (
    QueryRequest,
    QueryResponse
)


app = FastAPI(
    title="Document QA Assistant",
    version="1.0.0",
    description="Production Grade RAG Application"
)


# =========================
# LOAD PIPELINE ON STARTUP
# =========================

# Load PDF
documents = LoadPDF().load_pdf(
    PDF_PATH
)

# Split Documents
chunks = Splitter().split_documents(
    documents
)

# Load Embedding Model
embedding_model = EmbeddingModel()

embeddings = embedding_model.load_embedding_model()

# Create Vector Store
vectorstore = QdrantDB().create_vectorstore(
    chunks,
    embeddings
)

# Initialize RAG Pipeline
rag_pipeline = RAGPipeline()


# =========================
# ROOT ENDPOINT
# =========================

@app.get("/")
async def home():

    return {
        "message": "Document QA Assistant Running"
    }


# =========================
# HEALTH CHECK
# =========================

@app.get("/health")
async def health_check():

    return {
        "status": "healthy"
    }


# =========================
# QUESTION ANSWERING
# =========================

@app.post(
    "/ask",
    response_model=QueryResponse
)
async def ask_question(
    request: QueryRequest
):

    response = rag_pipeline.run_query(
        vectorstore,
        request.query
    )

    return QueryResponse(
        question=request.query,
        answer=response
    )