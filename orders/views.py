from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, redirect

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required(login_url='users:registration')
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)

        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            number=form.cleaned_data['number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )

                        total_price = 0

                        for cart_item in cart_items:
                            product = cart_item.product
                            name = product.name
                            price = product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(
                                    f'Недостатня кількість товару {name} в наявності — {product.quantity}'
                                )

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )

                            total_price += price * quantity

                            product.quantity -= quantity
                            product.save()

                        if request.user.email:
                            send_mail(
                                subject=f'Ваше замовлення №{order.id} прийнято',
                                message=f'''
Дякуємо за замовлення в інтернет-магазині Теремок!

Номер замовлення: {order.id}
Користувач: {request.user.username}
Телефон: {order.number}
Сума замовлення: {total_price} грн

Наш менеджер зв'яжеться з вами найближчим часом.
''',
                                from_email=settings.DEFAULT_FROM_EMAIL,
                                recipient_list=[request.user.email],
                                fail_silently=False,
                            )

                        send_mail(
                            subject=f'Нове замовлення №{order.id}',
                            message=f'''
Нове замовлення на сайті Теремок.

Номер замовлення: {order.id}
Користувач: {request.user.username}
Email користувача: {request.user.email}
Телефон: {order.number}
Сума замовлення: {total_price} грн
''',
                            from_email=settings.DEFAULT_FROM_EMAIL,
                            recipient_list=[settings.ADMIN_EMAIL],
                            fail_silently=False,
                        )

                        cart_items.delete()

                        messages.success(request, 'Замовлення створено')
                        return redirect('user:profile')

            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('cart:order')

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Home - Створення замовлення',
        'form': form,
    }

    return render(request, 'orders/create_order.html', context=context)