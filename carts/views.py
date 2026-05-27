from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_cart
from goods.models import Products


# Create your views here.
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
    user_cart = get_user_cart(request)
    cart_items_html = render_to_string(
         "carts/includes/cart_items.html",
        {"carts": user_cart},

        request=request
    )
    total_price = sum(float(cart.product.sell_price()) * cart.quantity for cart in user_cart)
    response_data = {
        "message": "Товар додан у кошик",
        "cart_items_html": cart_items_html,
        "total_price": total_price,
    }
    return JsonResponse(response_data)


def cart_change(request, product_slug):
    pass




def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])