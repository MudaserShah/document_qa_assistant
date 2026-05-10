from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.utils.logger import logger
import sys
from src.utils.exception import CustomException


class Splitter:

    def split_documents(self, documents):

        try:

            logger.info("Starting document splitting")

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=300,
                chunk_overlap=100
            )

            chunks = splitter.split_documents(documents)

            logger.info(
                f"Document splitting completed successfully. "
                f"Total chunks created: {len(chunks)}"
            )

            return chunks

        except Exception as e:

            logger.error(
                f"Error occurred while splitting documents: {str(e)}"
            )

            raise CustomException(e, sys)

