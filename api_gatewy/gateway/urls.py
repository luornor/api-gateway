from django.urls import path
from . views import (
    signup, 
    login, 
    getAndDeleteProfile, 
    listings, 
    listings_details, 
    shops,
    orders,
    orders_add,
    order_details,
    deliveries,
    delivery_details,
    CreateCart,
    CartItems,
    AddToCart
)


urlpatterns = [
    path("auth/signup/", signup),
    path("auth/login/", login),
    path("auth/users/<int:pk>/", getAndDeleteProfile),
    path("listings/", listings),
    path("listings/<int:pk>/", listings_details),
    path("shops/<int:pk>/", shops),
    path('cart/create/',CreateCart),
    path('cartItems/<int:user_id>/',CartItems),
    path('cart/add/',AddToCart),
    path("orders/", orders),
    path("orders/create/", orders_add),
    path("orders/<int:pk>/", order_details),
    path("deliveries/", deliveries),
    path("deliveries/<int:pk>/", delivery_details),
]
