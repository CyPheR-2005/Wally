// cart.js
document.addEventListener("DOMContentLoaded", () => {
  const checkoutBtn = document.querySelector("button");

  if (checkoutBtn) {
    checkoutBtn.addEventListener("click", () => {
      alert("🛍 Proceeding to checkout... (link to payment module here)");
    });
  }
});
