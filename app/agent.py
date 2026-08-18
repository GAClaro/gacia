from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()

STORE_NAME = os.getenv("FILE_SEARCH_STORE_NAME")

SYSTEM_INSTRUCTION = """
Você é o NexaAI, um assistente corporativo de perguntas e respostas.

Sua única fonte de informação são os documentos disponíveis
através do File Search.

REGRAS OBRIGATÓRIAS:

1. Nunca utilize seu conhecimento geral ou informações externas
   aos documentos.

2. Só responda uma pergunta se houver informação suficiente
   nos documentos.

3. Se a informação não estiver nos documentos, não tente
   responder utilizando conhecimento próprio.

4. Nesse caso, responda:
   "Não encontrei essa informação nos documentos disponíveis."

5. Não invente informações.

6. Responda de maneira clara, objetiva e profissional.
"""


def ask_agent(question: str) -> str:

    if not STORE_NAME:
        raise ValueError(
            "FILE_SEARCH_STORE_NAME não foi configurado no .env"
        )

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=f"""
{SYSTEM_INSTRUCTION}

Pergunta do usuário:
{question}
""",
        tools=[
            {
                "type": "file_search",
                "file_search_store_names": [STORE_NAME],
            }
        ],
    )

    for step in interaction.steps:
        if step.type == "model_output":
            for content in step.content:
                if content.type == "text":
                    return content.text

    return "Não foi possível gerar uma resposta."