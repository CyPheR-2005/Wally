// assistant.js
document.addEventListener("DOMContentLoaded", () => {
  const input = document.querySelector(".chat-input input");
  const button = document.querySelector(".chat-input button");
  const chatWindow = document.querySelector(".chat-window");

  button.disabled = false;
  input.disabled = false;

  button.addEventListener("click", () => {
    const message = input.value.trim();
    if (!message) return;

    // Display user message
    const userMsg = document.createElement("div");
    userMsg.className = "chat-message user";
    userMsg.innerHTML = `<p>${message}</p>`;
    chatWindow.appendChild(userMsg);

    // Simulate AI reply
    const aiMsg = document.createElement("div");
    aiMsg.className = "chat-message ai";
    aiMsg.innerHTML = `<p>🤖 Thinking... (replace with real LLM API)</p>`;
    chatWindow.appendChild(aiMsg);

    input.value = "";
    chatWindow.scrollTop = chatWindow.scrollHeight;
  });
});
