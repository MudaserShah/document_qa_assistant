from src.utils.logger import logger
import sys
from src.utils.exception import CustomException


class Retriever:

    def get_retriever(self, vectorstore):

        try:

            logger.info("Creating retriever")

            retriever = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 5, "fetch_k": 10}
            )

            logger.info(
                "Retriever created successfully"
            )

            return retriever

        except Exception as e:

            logger.error(
                f"Error creating retriever: {str(e)}"
            )

            raise CustomException(e, sys)