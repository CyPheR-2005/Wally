// reminders.js
document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".reminder-card button");

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      alert(`🔔 ${button.textContent} clicked`);
    });
  });
});
