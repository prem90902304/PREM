document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".js-yes-btn");
  const noBtn = document.querySelector(".js-no-btn");
  const questionContainer = document.querySelector(".question-container");
  const resultContainer = document.querySelector(".result-container");

  // Show question section on load
  questionContainer.classList.add("active");

  // When Yes is clicked
  yesBtn.addEventListener("click", () => {
    questionContainer.classList.remove("active");
    resultContainer.classList.add("active");
  });

  // Move Yes button on hover
  yesBtn.addEventListener("mouseover", () => {
    const container = document.querySelector(".button-container");
    const maxX = container.offsetWidth - yesBtn.offsetWidth;
    const maxY = container.offsetHeight - yesBtn.offsetHeight;

    const randomX = Math.random() * maxX;
    const randomY = Math.random() * maxY;

    yesBtn.style.left = `${randomX}px`;
    yesBtn.style.top = `${randomY}px`;
  });
});
