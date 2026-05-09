from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

from src.utils.logger import logger


class QdrantDB:

    def create_vectorstore(self, documents, embeddings, url: str, api_key: str):

        try:

            logger.info("Connecting to Qdrant Cloud cluster")

            client = QdrantClient(
                url=url,
                api_key=api_key,
            )

            logger.info(
                "Connected successfully. Creating vector store from documents"
            )

            vectorstore = QdrantVectorStore.from_documents(
                documents=documents,
                embedding=embeddings,
                url=url,
                api_key=api_key,
                collection_name="rag_collection",
                prefer_grpc=True,
            )

            logger.info(
                f"Vector store created successfully. "
                f"Total documents indexed: {len(documents)}"
            )

            return vectorstore

        except Exception as e:

            logger.error(
                f"Error occurred while creating Qdrant vector store: {str(e)}"
            )

            raise e

    def load_vectorstore(self, embeddings, url: str, api_key: str):

        try:

            logger.info("Loading existing Qdrant Cloud vector store")

            vectorstore = QdrantVectorStore.from_existing_collection(
                embedding=embeddings,
                url=url,
                api_key=api_key,
                collection_name="rag_collection",
                prefer_grpc=True,
            )

            logger.info("Vector store loaded successfully")

            return vectorstore

        except Exception as e:

            logger.error(
                f"Error occurred while loading Qdrant vector store: {str(e)}"
            )

            raise e