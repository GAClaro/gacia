from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


def ask_gemini(question: str, context: str) -> str:
    prompt = f"""
Você é o assistente virtual da NexaCloud.

Responda à pergunta do usuário utilizando exclusivamente
as informações presentes no contexto fornecido.

Se a resposta não estiver presente no contexto,
informe que não encontrou essa informação nos documentos.

Contexto:
{context}

Pergunta:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text