from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_cart
from goods.models import Products
def cart_add(request):
    product_id = request.POST.get('product_id')
    product = Products.objects.get(id=product_id)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(
            user=request.user,
            product=product
        )
        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(
                user=request.user,
                product=product,
                quantity=1
            )
    else:
        cart = Cart.objects.filter(
            session_key=request.session.session_key, product=product
        )
        if cart.exists():
            cart = cart.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(
                session_key=request.session.session_key,product=product,quantity=1
            )

    user_cart = get_user_cart(request)
    cart_items_html = render_to_string(
         "carts/includes/cart_items.html",
        {"carts": user_cart},

        request=request
    )
    total_price = sum(float(cart.product.sell_price()) * cart.quantity for cart in user_cart)
    cart_count = sum(cart.quantity for cart in user_cart)
    response_data = {
        "message": "Товар додано в кошик",
        "cart_items_html": cart_items_html,
        "total_price": total_price,
        "cart_count": cart_count,
    }
    return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")
    cart = Cart.objects.get(id=cart_id)
    cart.quantity = int(quantity)
    cart.save()
    user_cart = get_user_cart(request)
    total_price = sum(
        cart.product.sell_price() * cart.quantity
        for cart in user_cart
    )
    cart_items_html = render_to_string(
        "carts/includes/cart_items.html",
        {"carts": user_cart},
        request=request
    )
    response_data = {
        "message": "Кількість змінено",
        "cart_items_html": cart_items_html,
        "total_price": total_price,
    }
    return JsonResponse(response_data)

def cart_remove(request):
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.filter(id=cart_id).first()

    if not cart:
        return JsonResponse({"error": "not found"}, status=404)

    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_cart(request)

    cart_items_html = render_to_string(
        "carts/includes/cart_items.html",
        {"carts": user_cart},
        request=request
    )

    total_price = sum(
        cart.product.sell_price() * cart.quantity
        for cart in user_cart
    )

    return JsonResponse({
        "message": "Товар видалено",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
        "total_price": total_price,
    })