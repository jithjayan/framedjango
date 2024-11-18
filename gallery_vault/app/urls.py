from django.urls import path
from . import views


urlpatterns=[
    path('',views.ad_login),
    path('ad_home',views.ad_home),
    path('register',views.register),
    path('user_home',views.user_home),
    path('add_file',views.add_file),
    path('user_logout',views.user_logout),
    path('delete_file/<pid>',views.delete_file),


]