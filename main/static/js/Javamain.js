const rangeInput = document.querySelectorAll(".range-input input"),
      priceInput = document.querySelectorAll(".price-input input"),
      progress = document.querySelector(".slider .progress");

let priceGap = 1000;


let minVal = parseInt(rangeInput[0].value);
let maxVal = parseInt(rangeInput[1].value);


priceInput[0].value = minVal;
priceInput[1].value = maxVal;
progress.style.left = (minVal / rangeInput[0].max) * 100 + "%";
progress.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";

priceInput.forEach(input => {
    input.addEventListener("input", e => {
        minVal = parseInt(priceInput[0].value);
        maxVal = parseInt(priceInput[1].value);

        if ((maxVal - minVal >= priceGap) && maxVal <= rangeInput[1].max) {
            rangeInput[0].value = minVal;
            rangeInput[1].value = maxVal;
            progress.style.left = (minVal / rangeInput[0].max) * 100 + "%";
            progress.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
        }
    });
});

rangeInput.forEach(input => {
    input.addEventListener("input", e => {
        minVal = parseInt(rangeInput[0].value);
        maxVal = parseInt(rangeInput[1].value);

        if (maxVal - minVal < priceGap) {
            if (e.target.classList.contains("range-min")) {
                rangeInput[0].value = maxVal - priceGap;
                minVal = maxVal - priceGap;
            } else {
                rangeInput[1].value = minVal + priceGap;
                maxVal = minVal + priceGap;
            }
        }

        priceInput[0].value = minVal;
        priceInput[1].value = maxVal;
        progress.style.left = (minVal / rangeInput[0].max) * 100 + "%";
        progress.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
    });
});