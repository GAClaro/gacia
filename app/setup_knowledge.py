from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client()

STORE_NAME = os.getenv("FILE_SEARCH_STORE_NAME")

DOCUMENTS = [
    
    "documents/empresa.json",
    "documents/manual_nexacloud.md",
    "documents/manual_nexacloud.docx",
    "documents/planos.csv",
    "documents/politica_privacidade.md",
    "documents/politica_privacidade.pdf",
    "documents/politica_reembolso.md",
    "documents/politica_reembolso.pdf",
    "documents/tabela_precos.xlsx",
]


def setup_knowledge():

    if not STORE_NAME:
        raise ValueError(
            "FILE_SEARCH_STORE_NAME não foi configurado no .env"
        )

    print("===================================")
    print("GACIA - ATUALIZAÇÃO DA KNOWLEDGE BASE")
    print("===================================")

    print(f"\nStore utilizado:")
    print(STORE_NAME)

    print(f"\nDocumentos a enviar: {len(DOCUMENTS)}")

    for document in DOCUMENTS:

        if not os.path.exists(document):
            print(f"\n[ERRO] Arquivo não encontrado: {document}")
            continue

        print(f"\nEnviando: {document}")

        operation = client.file_search_stores.upload_to_file_search_store(
            file=document,
            file_search_store_name=STORE_NAME,
            config={
                "display_name": os.path.basename(document),
            },
        )

        print("Indexando...")

        while not operation.done:
            time.sleep(2)
            operation = client.operations.get(operation)

        print("OK - documento indexado!")

    print("\n===================================")
    print("KNOWLEDGE BASE ATUALIZADA")
    print("===================================")
    print(f"Store: {STORE_NAME}")
    print(f"Documentos processados: {len(DOCUMENTS)}")


if __name__ == "__main__":
    setup_knowledge()