function getCookie(name) {
    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");

        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}

const csrftoken = getCookie("csrftoken");

function animateCartButton() {
    const cartBtn = document.getElementById("open-cart");
    const cartCount = document.getElementById("goods-in-cart-count");

    if (cartBtn) {
        cartBtn.classList.remove("cart-btn--pulse");
        void cartBtn.offsetWidth;
        cartBtn.classList.add("cart-btn--pulse");
    }

    if (cartCount) {
        cartCount.classList.remove("cart-btn__count--pop");
        void cartCount.offsetWidth;
        cartCount.classList.add("cart-btn__count--pop");
    }
}

function showCartToast(message) {
    const toast = document.getElementById("jq-notification");
    if (!toast) {
        return;
    }

    toast.textContent = message;
    toast.hidden = false;
    toast.classList.add("cart-toast--visible");

    setTimeout(function () {
        toast.classList.remove("cart-toast--visible");
        setTimeout(function () {
            toast.hidden = true;
        }, 300);
    }, 3000);
}

$(document).ready(function () {
    $(document).on("click", ".add-to-cart", function (e) {
        e.preventDefault();

        const product_id = $(this).data("product-id");
        const add_to_cart_url = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: csrftoken,
            },
            success: function (data) {
                showCartToast(data.message);
                animateCartButton();

                if (typeof data.cart_count !== "undefined") {
                    const countEl = $("#goods-in-cart-count");
                    countEl.text(data.cart_count);
                    if (data.cart_count > 0) {
                        countEl.removeClass("cart-btn__count--empty");
                    } else {
                        countEl.addClass("cart-btn__count--empty");
                    }
                }

                $("#cart-items-container").html(data.cart_items_html);
                $("#cart-total-price strong").text(data.total_price);
            },
            error: function () {
                showCartToast("Не вдалося додати товар у кошик");
            },
        });
    });

    $(document).on("click", ".remove-from-cart", function (e) {
        e.preventDefault();

        const cart_id = $(this).data("cart-id");

        $.ajax({
            type: "POST",
            url: "/user/cart_remove/",
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: csrftoken,
            },
            success: function (data) {
                $("#cart-items-container").html(data.cart_items_html);
                $("#cart-total-price strong").text(data.total_price);

                const currentCount = parseInt($("#goods-in-cart-count").text() || "0", 10);
                const deleted = data.quantity_deleted || 0;
                $("#goods-in-cart-count").text(Math.max(0, currentCount - deleted));
            },
            error: function (xhr) {
                console.log("ERROR:", xhr.responseText);
            },
        });
    });

    $(document).on("click", ".decrement", function () {
        const url = $(this).data("cart-change-url");
        const cartID = $(this).data("cart-id");
        const quantityElement = $(this).siblings(".number");
        const currentQuantity = parseInt(quantityElement.text(), 10);

        if (currentQuantity > 1) {
            const newQuantity = currentQuantity - 1;
            quantityElement.text(newQuantity);
            updateCart(cartID, newQuantity, url);
        }
    });

    $(document).on("click", ".increment", function () {
        const url = $(this).data("cart-change-url");
        const cartID = $(this).data("cart-id");
        const quantityElement = $(this).siblings(".number");
        const currentQuantity = parseInt(quantityElement.text(), 10);
        const newQuantity = currentQuantity + 1;

        quantityElement.text(newQuantity);
        updateCart(cartID, newQuantity, url);
    });

    function updateCart(cartID, quantity, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: csrftoken,
            },
            success: function (data) {
                $("#cart-items-container").html(data.cart_items_html);
                $("#cart-total-price strong").text(data.total_price);
            },
            error: function (xhr) {
                console.log(xhr.responseText);
            },
        });
    }

    $("input[name='requires_delivery']").change(function () {
        const selectedValue = $(this).val();
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });
});
