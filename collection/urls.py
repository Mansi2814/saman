from django.contrib import admin
from django.urls import path
from collection import views

urlpatterns = [
    path('', views.index, name='index'),
    path('men/',views.men,name='men'),
    path('women/',views.women,name='women'),
    path('account/',views.account,name='account'),
    path('cart/',views.cart,name='cart'),
    path('addToCart/<str:product_id>/',views.addToCart,name='addToCart'),
    path('delete_cartItem/<str:product_id>/',views.delete_cartItem,name='delete_cartItem'),
    path('changeQuantity/<str:product_id>/',views.changeQuantity,name='change_quantity'),
    path('accessory/',views.accessory,name='accessory'),
    path('account/',views.account,name='account'),
    path('order_placed/',views.order_placed,name="order_placed")
]