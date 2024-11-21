from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from .models import *
# Create your views here.
def sample(req):
    d={'name':'aaa','age':11}
    return JsonResponse(d)

def user_def_serializer(req):
    if req.method=='GET':
        data=Student.objects.all()
        d=user_serializer(data,many=True)
        return JsonResponse(d.data,safe=False)