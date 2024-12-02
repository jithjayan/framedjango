from django.urls import path
from . import views
from django.contrib import admin


urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.m_login),
    path('logout',views.usr_logout),
    path('home',views.home),
    path('add',views.add),
    path('register',views.register),
]