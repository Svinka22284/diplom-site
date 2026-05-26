
const openCart = document.getElementById('open-cart');

const closeCart = document.getElementById('close-cart');

const cartSidebar = document.getElementById('cart-sidebar');

const cartOverlay = document.getElementById('cart-overlay');

openCart.addEventListener('click', () => {

    cartSidebar.classList.add('active');

    cartOverlay.classList.add('active');

});

closeCart.addEventListener('click', () => {

    cartSidebar.classList.remove('active');

    cartOverlay.classList.remove('active');

});

cartOverlay.addEventListener('click', () => {

    cartSidebar.classList.remove('active');

    cartOverlay.classList.remove('active');

});
