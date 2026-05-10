from langchain_openai import ChatOpenAI
from src.utils.exception import CustomException
import sys

from dotenv import load_dotenv

import os

from src.utils.logger import logger


load_dotenv()


class LoadLLM:

    def get_llm(self):

        try:

            logger.info("Loading OpenAI LLM")

            llm = ChatOpenAI(
                model="gpt-4o-mini",
                api_key=os.getenv("OPENAI_API_KEY")
            )

            logger.info("LLM loaded successfully")

            return llm

        except Exception as e:

            logger.error(
                f"Error loading LLM: {str(e)}"
            )

            raise CustomException(e, sys)