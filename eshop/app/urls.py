from django.urls import path
from . import views


urlpatterns=[

    path('',views.shop_login),
    path('shop_logout',views.shop_logout),

#---------------shop--------------
    path('shop_home',views.shop_home),
    path('add_product',views.add_product),
    path('edit_product/<pid>',views.edit_product),
    path('delete_product/<pid>',views.delete_product),
    path('bookings',views.bookings),

#---------------user--------------
    path('register',views.register),
    path('user_home',views.user_home),
    path('view_pro/<pid>',views.view_pro),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),
    path('delete_cart/<id>',views.delete_cart),
    path('user_buy/<cid>',views.user_buy),
    path('user_buy1/<pid>',views.user_buy1),
    path('user_bookings',views.user_bookings),

]