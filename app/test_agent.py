from .agent import ask_agent


question = "Quais planos possuem acesso à API?"

answer = ask_agent(question)

print("\nPergunta:")
print(question)

print("\nResposta:")
print(answer)