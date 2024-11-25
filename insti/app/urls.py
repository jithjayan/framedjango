from django.urls import path
from . import views


urlpatterns=[
    path('',views.instf),
    path('course',views.course),
    path('about',views.about),
    path('contact',views.contact),
    path('retrn',views.retrn),


]
