from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404,get_list_or_404
from goods.models import Products
# Create your views here.
def catalog(request,category_slug):
    page = request.GET.get('page',1)
    range_min = request.GET.get('range_min')
    range_max =request.GET.get('range_max')

    if category_slug == 'vse-tovary':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))


    if range_min and range_max:
        goods = goods.filter(price__gte=int(range_min),price__lte=int(range_max))
    goods = goods.order_by('price')
    paginator = Paginator(goods, 10)

    current_page = paginator.page(int(page))
    context = {
        'title':'Home- Каталог',
        'goods': current_page,
        "slug_url": category_slug,
}
    return render(request, 'goods/catalog.html',context)


def product(request,product_slug):

    product = Products.objects.get(slug=product_slug)
    context = {
        'product':product
    }
    return render(request, 'goods/product.html',context=context)