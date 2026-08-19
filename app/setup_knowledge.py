from google import genai
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client()


def setup_knowledge():
    print("Criando File Search Store...")

    store = client.file_search_stores.create(
        config={
            "display_name": "GACIA Knowledge Base",
            "embedding_model": "models/gemini-embedding-2",
        }
    )

    print(f"Store criado: {store.name}")

    print("Enviando documento...")

    operation = client.file_search_stores.upload_to_file_search_store(
        file="documents/faq.md",
        file_search_store_name=store.name,
        config={
            "display_name": "FAQ GACIA NexaCloud",
        },
    )

    print("Indexando documento...")

    while not operation.done:
        time.sleep(2)
        operation = client.operations.get(operation)

    print("Documento indexado com sucesso!")

    print("\n===================================")
    print("KNOWLEDGE BASE PRONTA")
    print("===================================")
    print(f"Store: {store.name}")


if __name__ == "__main__":
    setup_knowledge()
