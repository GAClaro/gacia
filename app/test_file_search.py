from google import genai
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client()

# 1. Criar o File Search Store
store = client.file_search_stores.create(
    config={
        "display_name": "NexaAI Teste",
        "embedding_model": "models/gemini-embedding-2",
    }
)

print(f"Store criado: {store.name}")

# 2. Fazer upload e indexar nosso FAQ
operation = client.file_search_stores.upload_to_file_search_store(
    file="documents/faq.md",
    file_search_store_name=store.name,
    config={
        "display_name": "FAQ NexaCloud",
    },
)

print("Indexando documento...")

# 3. Esperar a indexação terminar
while not operation.done:
    time.sleep(2)
    operation = client.operations.get(operation)

print("Documento indexado!")

# 4. Fazer uma pergunta
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="""
                Você é o NexaAI, um assistente corporativo de perguntas e respostas.

                Sua única fonte de informação são os documentos recuperados pela
                ferramenta File Search.

                REGRAS OBRIGATÓRIAS:

                1. Nunca utilize seu conhecimento geral ou informações externas
                aos documentos.

                2. Só responda uma pergunta se houver informação suficiente nos
                documentos recuperados pelo File Search.

                3. Se a informação não estiver nos documentos, NÃO tente responder
                com conhecimento próprio.

                4. Nesse caso, responda exatamente:
                "Não encontrei essa informação nos documentos disponíveis."

                5. Não invente informações.

                Pergunta do usuário:
                Qual é o preço da Netflix?
                """,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": [store.name],
        }
    ],
)

# 5. Mostrar resposta e citações
print("\nResposta:")

for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text":
                print(content.text)

                if content.annotations:
                    print("\nFontes:")

                    for annotation in content.annotations:
                        if annotation.type == "file_citation":
                            print(annotation)