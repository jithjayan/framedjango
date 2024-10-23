from django.urls import path
from . import views

urlpatterns=[
    path('fun1',views.fun1),
    path('fun2/<int:a>/<int:b>',views.fun2),
    path('tnum/<int:num>',views.tnum),
    path('city/<a>',views.city),
    path('day/<int:a>',views.day),
    path('bonus/<int:a>/<int:b>',views.bonus),
    path('tax/<int:a>',views.tax),
    path('bill/<int:a>',views.bill),
    path('demo',views.demo)
]