console.log("CATALOG JS LOADED");
document.addEventListener("DOMContentLoaded", function () {

    const btn = document.getElementById("catalogBtn");
    const menu = document.getElementById("catalogMenu");
    const wrapper = document.querySelector(".dropdown_meny_catalog");

    btn.addEventListener("click", function (e) {
        e.stopPropagation();
        wrapper.classList.toggle("active");
    });

    document.addEventListener("click", function () {
        wrapper.classList.remove("active");
    });

    menu.addEventListener("click", function (e) {
        e.stopPropagation();
    });

});