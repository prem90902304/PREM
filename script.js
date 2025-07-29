document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".js-yes-btn");
  const noBtn = document.querySelector(".js-no-btn");
  const questionContainer = document.querySelector(".question-container");
  const resultContainer = document.querySelector(".result-container");

  // Show the question screen
  questionContainer.style.display = "block";
  resultContainer.style.display = "none";

  // YES button click → Show result
  yesBtn.addEventListener("click", () => {
    questionContainer.style.display = "none";
    resultContainer.style.display = "block";
  });

  // Move YES button randomly on hover
  yesBtn.addEventListener("mouseenter", () => {
    const container = document.querySelector(".button-container");
    const maxX = container.offsetWidth - yesBtn.offsetWidth;
    const maxY = container.offsetHeight - yesBtn.offsetHeight;

    const randomX = Math.floor(Math.random() * maxX);
    const randomY = Math.floor(Math.random() * maxY);

    yesBtn.style.position = "absolute";
    yesBtn.style.left = `${randomX}px`;
    yesBtn.style.top = `${randomY}px`;
  });
});
