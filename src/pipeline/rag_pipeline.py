import os
from langchain_core.prompts import ChatPromptTemplate
from src.components.retriever import Retriever
from src.components.llm import LoadLLM
from src.components.embeddings import EmbeddingModel
from src.components.vectorstore import QdrantDB
from src.utils.logger import logger
import sys
from src.utils.exception import CustomException

SYSTEM_PROMPT = """You are a helpful assistant that answers questions based on the provided context.

Rules:
- Answer only from the retrieved context
- If numbers or data are present in the context, perform calculations when asked
- If the answer is truly not in the context, say "This information is not available in the document"
- Never say you "cannot" do something if the data is already in the context
- Keep answers concise and accurate"""

HUMAN_PROMPT = """Context:
{context}

Question:
{question}"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", HUMAN_PROMPT)
])


class RAGPipeline:

    def load_vectorstore(self):

        try:

            logger.info("Loading existing vector store")

            embed = EmbeddingModel()
            embedding_model = embed.load_embedding_model()

            db = QdrantDB()
            vectorstore = db.load_vectorstore(
                embeddings=embedding_model,
                url=os.getenv("QDRANT_URL"),
                api_key=os.getenv("QDRANT_API_KEY")
            )

            logger.info("Vector store loaded successfully")

            return vectorstore

        except Exception as e:

            logger.error(f"Error loading vector store: {str(e)}")

            raise CustomException(e, sys)

    def run_query(self, vectorstore, query):

        try:

            logger.info(f"Running RAG query: {query}")

            retriever = Retriever().get_retriever(vectorstore)

            docs = retriever.invoke(query)

            logger.info(f"Retrieved {len(docs)} relevant chunks")

            context = "\n\n".join([doc.page_content for doc in docs])

            llm = LoadLLM().get_llm()

            prompt = prompt_template.invoke({
                "context": context,
                "question": query
            })

            response = llm.invoke(prompt)

            logger.info("LLM response generated successfully")

            return response.content

        except Exception as e:

            logger.error(f"Error in RAG pipeline: {str(e)}")

            raise CustomException(e, sys)