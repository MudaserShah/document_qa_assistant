from dotenv import load_dotenv

load_dotenv()

from src.pipeline.rag_pipeline import RAGPipeline

if __name__ == "__main__":

    rag = RAGPipeline()
    vectorstore = rag.load_vectorstore()

    print("💬 Chatbot ready! Type 'exit' to quit.\n")

    while True:

        query = input("Ask Question: ").strip()

        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if not query:
            continue

        response = rag.run_query(vectorstore, query)

        print(f"\nAnswer:\n{response}\n")