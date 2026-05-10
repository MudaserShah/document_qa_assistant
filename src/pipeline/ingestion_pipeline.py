import os
from dotenv import load_dotenv

load_dotenv()
import sys
from src.components.loader import LoadPDF
from src.components.splitter import Splitter
from src.components.embeddings import EmbeddingModel
from src.components.vectorstore import QdrantDB
from src.utils.logger import logger
from src.config import PDF_PATH
from src.utils.exception import CustomException

class IngestionPipeline:

    def run_pipeline(self):

        try:

            logger.info("Starting ingestion pipeline")

            loader = LoadPDF()
            documents = loader.load_pdf(PDF_PATH
            )

            splitter = Splitter()
            split_document = splitter.split_documents(documents=documents)

            texts = [doc.page_content for doc in split_document]

            embed = EmbeddingModel()
            embedding = embed.get_embeddings(texts)

            db = QdrantDB()
            vectorstore = db.create_vectorstore(
                documents=split_document,
                embeddings=embedding,
            )

            logger.info("Ingestion pipeline completed successfully")

            return vectorstore

        except Exception as e:

            logger.error(f"Error in ingestion pipeline: {str(e)}")

            raise CustomException(e, sys)