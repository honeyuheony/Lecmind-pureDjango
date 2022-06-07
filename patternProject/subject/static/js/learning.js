document.addEventListener("DOMContentLoaded", () => {
    const SAVING_MESSAGE = "저장중...";
    const SAVED_MESSAGE = "저장 완료";
  
    document
      .querySelectorAll(".autosave-message")
      .forEach((el) => (el.textContent = SAVED_MESSAGE));
  
    document.querySelectorAll("[data-autosave-url]").forEach((inputField) => {
      inputField.addEventListener("change", async () => {
        const name = inputField.getAttribute("name");
        const value = inputField.value;
        const url = inputField.dataset.autosaveUrl;
        const autosaveMessageEl = inputField
          .closest(".writing")
          .querySelector(".autosave-message");
        const formData = new FormData();
  
        formData.append(name, value);
        autosaveMessageEl.classList.add("autosave-message--saving");
        autosaveMessageEl.textContent = SAVING_MESSAGE;
  
        const response = await fetch(url, {
          method: "POST",
          body: formData
        });
  
        autosaveMessageEl.classList.remove("autosave-message--saving");
        autosaveMessageEl.textContent = SAVED_MESSAGE;
      });
    });
  });
  