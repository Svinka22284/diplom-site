(function () {
    "use strict";

    document.querySelectorAll("input, textarea, select").forEach(function (field) {
        field.addEventListener("input", function () {
            field.classList.remove("is-invalid");
        });
        field.addEventListener("change", function () {
            field.classList.remove("is-invalid");
        });
    });
})();
