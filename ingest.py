from src.pipeline.ingestion_pipeline import IngestionPipeline

if __name__ == "__main__":

    pipeline = IngestionPipeline()
    pipeline.run_pipeline()

    print("✅ Documents indexed successfully. Now run main.py to chat.")