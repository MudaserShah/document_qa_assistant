import os

from dotenv import load_dotenv

from langchain_qdrant import QdrantVectorStore

from src.utils.logger import logger
import sys
from src.utils.exception import CustomException


load_dotenv()


class QdrantDB:

    def create_vectorstore(
        self,
        documents,
        embeddings
    ):

        try:

            logger.info(
                "Creating Qdrant vectorstore"
            )

            vectorstore = QdrantVectorStore.from_documents(
                documents=documents,
                embedding=embeddings,
                url=os.getenv("QDRANT_URL"),
                api_key=os.getenv("QDRANT_API_KEY"),
                collection_name="rag_collection"
            )

            logger.info(
                "Vectorstore created successfully"
            )

            return vectorstore

        except Exception as e:

            logger.exception(
                f"Error creating vectorstore: {str(e)}"
            )

            raise CustomException(e, sys)