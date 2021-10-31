from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register_reception/', views.register_reception, name="register_reception"),
    path('reception_formpage/', views.reception_formpage, name="reception_formpage")
]