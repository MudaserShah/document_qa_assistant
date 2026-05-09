from langchain_huggingface import HuggingFaceEmbeddings
from src.utils.logger import logger


class EmbeddingModel:

    def load_embedding_model(self):

        try:

            logger.info("Loading HuggingFace Embeddings model: sentence-transformers/all-MiniLM-L6-v2")

            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )

            logger.info("Embedding model loaded successfully")

            return embeddings

        except Exception as e:

            logger.exception(f"Failed to load embedding model: {str(e)}")

            raise e

    def get_embeddings(self, chunks):

        try:

            logger.info("Starting document embedding")

            embeddings = self.load_embedding_model()

            vectors = embeddings.embed_documents(chunks)

            logger.info("Embeddings created successfully")

            return embeddings

        except Exception as e:

            logger.exception(f"Failed to create embeddings: {str(e)}")

            raise e