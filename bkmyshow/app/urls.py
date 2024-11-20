from django.urls import path
from . import views


urlpatterns=[
    path('',views.homepage),
    path('view_movie',views.view_movie),
]