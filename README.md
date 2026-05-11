# Document QA Assistant

An AI-powered Document Question Answering Assistant built with FastAPI, LangChain, Qdrant, and OpenAI embeddings. This project allows users to upload documents, create vector embeddings, store them in Qdrant, and ask questions about the uploaded content using Retrieval-Augmented Generation (RAG).

---

# Features

* Upload PDF documents
* Extract and split document text
* Generate embeddings using OpenAI
* Store embeddings in Qdrant Vector Database
* Ask questions from uploaded documents
* FastAPI backend APIs
* Scalable RAG architecture
* Persistent vector storage support
* Production-ready modular structure

---

# Tech Stack

## Backend

* Python
* FastAPI
* Uvicorn

## AI / RAG

* LangChain
* OpenAI Embeddings
* Retrieval-Augmented Generation (RAG)

## Vector Database

* Qdrant

## Utilities

* Python-dotenv
* Pydantic
* Logging

---

# Project Structure

````bash
document_qa_assistant/
│
├── artifacts/
│   └── vectorstore/
│
├── data/
│
├── logs/
│
├── notebooks/
│   └── rag_chain.ipynb
│
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── embeddings.py
│   │   ├── llm.py
│   │   ├── loader.py
│   │   ├── retriever.py
│   │   ├── splitter.py
│   │   └── vectorstore.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── ingestion_pipeline.py
│   │   └── rag_pipeline.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── exception.py
│       ├── logger.py
│       ├── config.py
│       └── schema.py
│
├── venv/
├── .dockerignore
├── .env
├── .gitignore
├── app.py
├── ingest.py
├── main.py
├── Dockerfile
├── requirements.txt
└── README.md

# Installation

## 1. Clone Repository

```bash
git clone <your-github-repo-link>
cd Document_QA_Assistant
```

---

## 2. Create Virtual Environment

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
OPENAI_API_KEY=your_openai_api_key
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_URL=your_qdrant_url
COLLECTION_NAME=document_qa
```

---

# Running the Application

## Start FastAPI Server

```bash
uvicorn app:app --reload
```

Server will run on:

```bash
http://127.0.0.1:8000
```

---

# API Endpoints

## Home Endpoint

```http
GET /
```

Returns API status.

---

## Upload Document

```http
POST /upload
```

Uploads and processes documents.

---

## Ask Questions

```http
POST /ask
```

Example Request:

```json
{
  "query": "What is name of document?"
}
```

Example Response:

```json
{
  "answer": "The document name is..."
}
```

---

# How It Works

1. User uploads documents
2. Documents are loaded and split into chunks
3. Embeddings are generated using OpenAI
4. Embeddings are stored in Qdrant
5. User asks questions
6. Relevant chunks are retrieved
7. LLM generates final answer

---

# Future Improvements

* Streamlit frontend
* Multi-document support
* Authentication system
* Chat history memory
* Hybrid search
* Multi-modal document support
* Docker deployment
* Kubernetes deployment
* CI/CD pipeline

---

# Example Use Cases

* Research assistant
* Company knowledge base
* Legal document analysis
* Medical document search
* Educational chatbot
* PDF-based AI assistant

---

# Requirements

```txt
fastapi
uvicorn
langchain
langchain-openai
qdrant-client
python-dotenv
openai
pypdf
```

---

# Author

Syed
AI Engineer | Data Science Learner | Agentic AI Builder

