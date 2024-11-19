from django.urls import path
from . import views


urlpatterns=[
    path('user_def_form',views.user_def_form),
    path('modelform_fun',views.modelform_fun)
]