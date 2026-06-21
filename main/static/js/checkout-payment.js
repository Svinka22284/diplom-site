(function () {
    "use strict";

    const form = document.getElementById("checkoutForm");
    if (!form) {
        return;
    }

    const paymentRadios = form.querySelectorAll('input[name="payment_on_get"]');
    const cardForm = document.getElementById("cardPaymentForm");
    const cardNumber = document.getElementById("cardNumber");
    const cardHolder = document.getElementById("cardHolder");
    const cardExpiry = document.getElementById("cardExpiry");
    const cardCvv = document.getElementById("cardCvv");

    const errors = {
        cardNumber: document.getElementById("cardNumberError"),
        cardHolder: document.getElementById("cardHolderError"),
        cardExpiry: document.getElementById("cardExpiryError"),
        cardCvv: document.getElementById("cardCvvError"),
    };

    function isCardPaymentSelected() {
        const selected = form.querySelector('input[name="payment_on_get"]:checked');
        return selected && selected.value === "0";
    }

    function toggleCardForm() {
        if (!cardForm) {
            return;
        }

        const show = isCardPaymentSelected();
        cardForm.classList.toggle("is-visible", show);
        cardForm.setAttribute("aria-hidden", show ? "false" : "true");

        if (!show) {
            clearCardErrors();
            [cardNumber, cardHolder, cardExpiry, cardCvv].forEach(function (input) {
                if (input) {
                    input.classList.remove("is-invalid");
                    input.value = "";
                }
            });
        }
    }

    function clearCardErrors() {
        Object.keys(errors).forEach(function (key) {
            if (errors[key]) {
                errors[key].innerHTML = "";
                errors[key].classList.remove("form-error-msg--visible");
            }
        });
    }

    function clearFieldSuccess(fieldKey, input) {
        if (input) {
            input.classList.remove("is-invalid");
        }
        if (errors[fieldKey]) {
            errors[fieldKey].innerHTML = "";
            errors[fieldKey].classList.remove("form-error-msg--visible");
        }
    }

    function hasFieldError(fieldKey) {
        return errors[fieldKey] && errors[fieldKey].classList.contains("form-error-msg--visible");
    }

    function setError(fieldKey, message) {
        const inputMap = {
            cardNumber: cardNumber,
            cardHolder: cardHolder,
            cardExpiry: cardExpiry,
            cardCvv: cardCvv,
        };

        if (errors[fieldKey]) {
            if (message) {
                errors[fieldKey].innerHTML =
                    '<span class="form-error-msg__icon" aria-hidden="true">⚠</span>' +
                    '<span class="form-error-msg__text">' + message + "</span>";
                errors[fieldKey].classList.add("form-error-msg--visible");
            } else {
                errors[fieldKey].innerHTML = "";
                errors[fieldKey].classList.remove("form-error-msg--visible");
            }
        }
        if (inputMap[fieldKey]) {
            if (message) {
                inputMap[fieldKey].classList.add("is-invalid");
            } else {
                inputMap[fieldKey].classList.remove("is-invalid");
            }
        }
    }

    function formatCardNumber(value) {
        const digits = value.replace(/\D/g, "").slice(0, 16);
        return digits.replace(/(\d{4})(?=\d)/g, "$1 ").trim();
    }

    function formatExpiry(value) {
        const digits = value.replace(/\D/g, "").slice(0, 4);
        if (digits.length <= 2) {
            return digits;
        }
        return digits.slice(0, 2) + "/" + digits.slice(2);
    }

    function validateCardNumber() {
        const digits = cardNumber.value.replace(/\D/g, "");
        if (!digits.length) {
            setError("cardNumber", "Введіть номер картки");
            return false;
        }
        if (!/^\d+$/.test(digits)) {
            setError("cardNumber", "Номер картки повинен містити тільки цифри");
            return false;
        }
        if (digits.length !== 16) {
            setError("cardNumber", "Номер картки повинен містити 16 цифр");
            return false;
        }
        clearFieldSuccess("cardNumber", cardNumber);
        return true;
    }

    function validateCardHolder() {
        const value = cardHolder.value.trim();
        if (!value) {
            setError("cardHolder", "Введіть ім'я власника картки");
            return false;
        }
        if (!/^[A-Za-zА-Яа-яІіЇїЄєҐґ\s]+$/.test(value)) {
            setError("cardHolder", "Допускаються лише літери та пробіли");
            return false;
        }
        clearFieldSuccess("cardHolder", cardHolder);
        return true;
    }

    function validateExpiry() {
        const value = cardExpiry.value.trim();
        if (!/^\d{2}\/\d{2}$/.test(value)) {
            setError("cardExpiry", "Введіть термін у форматі MM/YY");
            return false;
        }

        const month = parseInt(value.slice(0, 2), 10);
        if (month < 1 || month > 12) {
            setError("cardExpiry", "Місяць повинен бути від 01 до 12");
            return false;
        }

        clearFieldSuccess("cardExpiry", cardExpiry);
        return true;
    }

    function validateCvv() {
        const digits = cardCvv.value.replace(/\D/g, "");
        if (!digits.length) {
            setError("cardCvv", "Введіть CVV");
            return false;
        }
        if (digits.length < 3 || digits.length > 4) {
            setError("cardCvv", "CVV повинен містити 3 або 4 цифри");
            return false;
        }
        clearFieldSuccess("cardCvv", cardCvv);
        return true;
    }

    function validateCardForm() {
        clearCardErrors();
        const results = [
            validateCardNumber(),
            validateCardHolder(),
            validateExpiry(),
            validateCvv(),
        ];
        return results.every(Boolean);
    }

    paymentRadios.forEach(function (radio) {
        radio.addEventListener("change", toggleCardForm);
    });
    toggleCardForm();

    if (cardNumber) {
        cardNumber.addEventListener("input", function () {
            cardNumber.value = formatCardNumber(cardNumber.value);
            if (hasFieldError("cardNumber")) {
                validateCardNumber();
            }
        });
    }

    if (cardHolder) {
        cardHolder.addEventListener("input", function () {
            cardHolder.value = cardHolder.value.replace(/[^A-Za-zА-Яа-яІіЇїЄєҐґ\s]/g, "");
            if (hasFieldError("cardHolder")) {
                validateCardHolder();
            }
        });
    }

    if (cardExpiry) {
        cardExpiry.addEventListener("input", function () {
            cardExpiry.value = formatExpiry(cardExpiry.value);
            if (hasFieldError("cardExpiry")) {
                validateExpiry();
            }
        });
    }

    if (cardCvv) {
        cardCvv.addEventListener("input", function () {
            cardCvv.value = cardCvv.value.replace(/\D/g, "").slice(0, 4);
            if (hasFieldError("cardCvv")) {
                validateCvv();
            }
        });
    }

    form.addEventListener("submit", function (event) {
        if (!isCardPaymentSelected()) {
            return;
        }

        if (!validateCardForm()) {
            event.preventDefault();
        }
    });
})();
