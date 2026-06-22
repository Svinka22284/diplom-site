// Коли html-документ готовий (відмальований)
$(document).ready(function () {
    // Беремо з розмітки елемент за id — сповіщення від django
    var notification = $('#notification');
    // І через 7 сек. прибираємо
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }

    // При кліку на значок кошика відкриваємо спливаюче (модальне) вікно
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Подія кліку по кнопці закриття вікна кошика
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Обробник події радіокнопки вибору способу доставки
    $("input[name='requires_delivery']").change(function() {
        var selectedValue = $(this).val();
        // Ховаємо або показуємо поле введення адреси доставки
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

});
