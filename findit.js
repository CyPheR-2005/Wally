// findit.js
document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card");

  cards.forEach(card => {
    card.addEventListener("click", () => {
      const product = card.querySelector("h3").textContent;
      alert(`📍 Showing map for ${product}`);
    });
  });
});
