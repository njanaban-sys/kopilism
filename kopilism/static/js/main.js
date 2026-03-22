// Kopilism — main.js

// Auto-dismiss flash messages after 4s
document.addEventListener('DOMContentLoaded', () => {
  const messages = document.querySelectorAll('.message');
  messages.forEach(msg => {
    setTimeout(() => {
      msg.style.opacity = '0';
      msg.style.transition = 'opacity 0.5s';
      setTimeout(() => msg.remove(), 500);
    }, 4000);
  });
});
