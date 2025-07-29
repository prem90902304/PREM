document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".js-yes-btn");
  const noBtn = document.querySelector(".js-no-btn");
  const questionContainer = document.querySelector(".question-container");
  const resultContainer = document.querySelector(".result-container");
  const resultHeading = resultContainer.querySelector("h2");
  const container = document.querySelector(".button-container");

  questionContainer.style.display = "block";
  resultContainer.style.display = "none";

  let autoRevealTimeout;

  // Function to show the result with custom message
  function showResult(message) {
    questionContainer.style.display = "none";
    resultHeading.textContent = message;
    resultContainer.style.display = "block";
  }

  // When Yes is clicked (if possible)
  yesBtn.addEventListener("click", () => {
    clearTimeout(autoRevealTimeout);
    showResult("I knew it!");
  });

  // No button clicked (optional behavior)
  noBtn.addEventListener("click", () => {
    clearTimeout(autoRevealTimeout);
    showResult("😢 So sad... but okay.");
  });

  // Move Yes button randomly
  function moveYesButton() {
    const maxX = container.offsetWidth - yesBtn.offsetWidth;
    const maxY = container.offsetHeight - yesBtn.offsetHeight;
    const newX = Math.random() * maxX;
    const newY = Math.random() * maxY;
    yesBtn.style.position = "absolute";
    yesBtn.style.left = `${newX}px`;
    yesBtn.style.top = `${newY}px`;
  }

  // Mouse escape
  document.addEventListener("mousemove", (e) => {
    const mouseX = e.clientX;
    const mouseY = e.clientY;
    const btnRect = yesBtn.getBoundingClientRect();
    const btnX = btnRect.left + btnRect.width / 2;
    const btnY = btnRect.top + btnRect.height / 2;
    const distance = Math.hypot(mouseX - btnX, mouseY - btnY);
    if (distance < 120) moveYesButton();
  });

  // Touch escape (mobile)
  yesBtn.addEventListener("touchstart", (e) => {
    e.preventDefault();
    moveYesButton();
  });

  // 💔 Auto show "you don't have love" after 10 seconds
  autoRevealTimeout = setTimeout(() => {
    showResult("I knew it, you don't have love 💔");
  }, 10000); // 10 seconds
});
