const button = document.getElementById("ask-button");
const questionInput = document.getElementById("question");
const answer = document.getElementById("answer");

button.addEventListener("click", async () => {

    const question = questionInput.value.trim();

    if (!question) {
        answer.textContent = "Digite uma pergunta.";
        return;
    }

    answer.textContent = "Consultando documentos...";

    try {

        const response = await fetch("/ask", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        answer.textContent = data.answer;

    } catch (error) {

        answer.textContent =
            "Ocorreu um erro ao consultar o NexaAI.";

    }
});