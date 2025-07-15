// index.js
function toggleChatbot() {
  const container = document.getElementById("chatbot-container");
  container.classList.toggle("hidden");
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("chatbot-launcher")?.addEventListener("click", toggleChatbot);
  document.querySelector("#chatbot-container .secondary")?.addEventListener("click", toggleChatbot);
});
