from django import template

from carts.models import Cart
from carts.utils import get_user_cart

register = template.Library()


@register.simple_tag()
def user_carts(request):
    return get_user_cart(request)


@register.simple_tag()
def cart_items_count(request):
    cart = get_user_cart(request)
    return sum(item.quantity for item in cart)