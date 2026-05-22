from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('avtorizeytion/', views.avtorizeytion, name='avtorizeytion'),
    path('profile/', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
]
