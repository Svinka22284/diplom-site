document.addEventListener("DOMContentLoaded", () => {

  const selectBtn = document.querySelector(".select-btn");
  const items = document.querySelectorAll(".item");
  const btnText = document.querySelector(".btn-text");

  if (!selectBtn) return;

  selectBtn.addEventListener("click", () => {
    selectBtn.classList.toggle("open");
  });

  items.forEach(item => {
    item.addEventListener("click", () => {

      item.classList.toggle("checked");

      const checkedItems =
        document.querySelectorAll(".item.checked");

      if (checkedItems.length > 0) {
        btnText.innerText =
          `${checkedItems.length} обрано`;
      } else {
        btnText.innerText = "Бренди";
      }

    });
  });

});

