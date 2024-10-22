from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(req):
    return HttpResponse("welcome")
def fun2(reg,a,b):
    
    return HttpResponse(a,b)
def tnum(req,num):

    a=num%10
    if a==0:
        return HttpResponse("not divisible by 3")
    elif a%3==0:
        return HttpResponse("divisible by 3")
    else:
        return HttpResponse("not divisible by 3")
def city(req,city):
    ct=input("enter city :")
    ct=ct.lower()
    if ct=='delhi':
        print("monuments : Red Fort")
    elif ct=='agra' :
        print("monuments : Taj Mahal")
    elif ct=="jaipur":
        print("monuments : jal mahal")
    else:
        print("no munuments")