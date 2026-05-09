import os
from dotenv import load_dotenv

load_dotenv()

from src.components.loader import LoadPDF
from src.components.splitter import Splitter
from src.components.embeddings import EmbeddingModel
from src.components.vectorstore import QdrantDB
from src.utils.logger import logger


class IngestionPipeline:

    def run_pipeline(self):

        try:

            logger.info("Starting ingestion pipeline")

            loader = LoadPDF()
            documents = loader.load_pdf(
                "/home/syed-mudaser-mazhar/document_qa_assistant/data/document.pdf"
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
                url=os.getenv("QDRANT_URL"),
                api_key=os.getenv("QDRANT_API_KEY")
            )

            logger.info("Ingestion pipeline completed successfully")

            return vectorstore

        except Exception as e:

            logger.error(f"Error in ingestion pipeline: {str(e)}")

            raise e