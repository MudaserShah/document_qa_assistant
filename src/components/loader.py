from langchain_community.document_loaders import PyPDFLoader
import sys
from src.utils.logger import logger
from src.utils.exception import CustomException

class LoadPDF:

    def load_pdf(self, file_path):

        try:

            logger.info(
                f"Starting PDF loading from: {file_path}"
            )

            loader = PyPDFLoader(file_path)

            documents = loader.load()

            logger.info(
                f"PDF loaded successfully. Total pages: {len(documents)}"
            )

            return documents

        except Exception as e:

            logger.error(
                f"Error occurred while loading PDF: {str(e)}"
            )

            raise CustomException(e, sys)