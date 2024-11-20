from django.shortcuts import render
from .models import *
# Create your views here.
def homepage(req):
    data=Movie.objects.all()[::-1]
    return render(req,'homepage.html',{'Movie':data})

def view_movie(req,pid):
    data=Movie.objects.get(pk=pid)
    return render(req,'secpage.html',{'Movie':data})