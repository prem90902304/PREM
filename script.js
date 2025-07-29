const yesBtn = document.querySelector(".js-yes-btn");
const noBtn = document.querySelector(".js-no-btn");
const resultContainer = document.querySelector(".result-container");
const questionContainer = document.querySelector(".question-container");

yesBtn.addEventListener("mouseover", () => {
  const i = Math.floor(Math.random() * 300) + 1;
  const j = Math.floor(Math.random() * 300) + 1;

  yesBtn.style.left = i + "px";
  yesBtn.style.top = j + "px";
});

yesBtn.addEventListener("click", () => {
  questionContainer.style.display = "none";
  resultContainer.style.display = "block";
});

// Show message after 10s, hide after 2s
setTimeout(() => {
  const message = document.getElementById("timeout-message");
  if (message) {
    message.style.display = "block";
    setTimeout(() => {
      message.style.display = "none";
    }, 2000);
  }
}, 10000);
