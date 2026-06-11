
const openCart = document.getElementById('open-cart');

const closeCart = document.getElementById('close-cart');

const cartSidebar = document.getElementById('cart-sidebar');

const cartOverlay = document.getElementById('cart-overlay');

function closeCartSidebar() {
    cartSidebar.classList.remove('active');
    cartOverlay.classList.remove('active');
    openCart.classList.remove('cart-btn--hidden');
}

openCart.addEventListener('click', () => {
    cartSidebar.classList.add('active');
    cartOverlay.classList.add('active');
    openCart.classList.add('cart-btn--hidden');
});

closeCart.addEventListener('click', closeCartSidebar);

cartOverlay.addEventListener('click', closeCartSidebar);
