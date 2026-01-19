from django import template

from goods.models import Categories

register = template.Library()

@register.simple_tag()
def tagcategories():
    return Categories.objects.all()