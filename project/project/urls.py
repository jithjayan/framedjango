"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fun1',views.fun1),
    path('fun2/<int:a>/<int:b>',views.fun2),
    path('tnum/<int:num>',views.tnum),
    path('city/<a>',views.city),
    path('day/<int:a>',views.day),
    path('bonus/<int:a>/<int:b>',views.bonus),
    path('tax/<int:a>',views.tax),
    path('bill/<int:a>',views.bill),
    
]
