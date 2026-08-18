from .gemini import ask_gemini
from .knowledge import load_document


chunks = load_document("documents/faq.md")

context = "\n\n".join(chunks)

question = "Quais planos possuem acesso à API?"

answer = ask_gemini(question, context)

print("\nPergunta:")
print(question)

print("\nResposta:")
print(answer)