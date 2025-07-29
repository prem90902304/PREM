document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".js-yes-btn");
  const noBtn = document.querySelector(".js-no-btn");
  const questionContainer = document.querySelector(".question-container");
  const resultContainer = document.querySelector(".result-container");
  const resultHeading = resultContainer.querySelector("h2");
  const container = document.querySelector(".button-container");

  questionContainer.style.display = "flex";
  resultContainer.style.display = "none";

  let autoRevealTimeout;

  function showResult(message) {
    clearTimeout(autoRevealTimeout);
    questionContainer.style.display = "none";
    resultHeading.textContent = message;
    resultContainer.style.display = "flex";
  }

  yesBtn.addEventListener("click", () => {
    showResult("I knew it!");
  });

  noBtn.addEventListener("click", () => {
    showResult("😢 So sad... but okay.");
  });

  function moveYesButton() {
    const maxX = container.offsetWidth - yesBtn.offsetWidth;
    const maxY = container.offsetHeight - yesBtn.offsetHeight;
    const newX = Math.random() * maxX;
    const newY = Math.random() * maxY;
    yesBtn.style.left = `${newX}px`;
    yesBtn.style.top = `${newY}px`;
  }

  document.addEventListener("mousemove", (e) => {
    const mouseX = e.clientX;
    const mouseY = e.clientY;
    const btnRect = yesBtn.getBoundingClientRect();
    const btnX = btnRect.left + btnRect.width / 2;
    const btnY = btnRect.top + btnRect.height / 2;
    const distance = Math.hypot(mouseX - btnX, mouseY - btnY);
    if (distance < 100) moveYesButton();
  });

  yesBtn.addEventListener("touchstart", (e) => {
    e.preventDefault();
    moveYesButton();
  });

  // ⏳ Auto show "no love" message after 10s, disappear after 2s
  autoRevealTimeout = setTimeout(() => {
    const message = document.getElementById("timeout-message");
    if (message && questionContainer.style.display !== "none") {
      message.style.display = "block";
      setTimeout(() => {
        message.style.display = "none";
      }, 2000);
    }
  }, 10000);
});
