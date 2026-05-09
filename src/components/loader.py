from langchain_community.document_loaders import PyPDFLoader

from src.utils.logger import logger

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

            raise e