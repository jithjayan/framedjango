from django.urls import path
from . import views


urlpatterns=[
    path('',views.homepage),
    path('view_movie/<pid>',views.view_movie),
]