from django.urls import path

from orders import views

app_name = "orders"

urlpatterns = [
    path('create-orders/', views.create_order, name="create_order"),
]