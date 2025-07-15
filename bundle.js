// bundle.js
document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".card button");

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      alert("✔️ Combo added to cart!");
    });
  });
});
