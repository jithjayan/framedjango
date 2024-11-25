from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.models import User
import os
from django.contrib import messages
# Create your views here.
def instf(req):
    return render(req,'main.html')

def course(req):
    data=Course.objects.all()
    return render(req,'course.html',{'Course':data})
    
def about(req):
    return render(req,'about.html')
def contact(req):
    return render(req,'contact.html')

def cnct(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email'] 
        phnum=req.POST['phnum']
        msg=req.POST['msg']       
        try:
            data=User.objects.create_user(first_name=name,email=email,phnum=phnum,msg=msg)
            data.save()
            return redirect(contact)
        except:
            messages.warning(req,"Email already exist")
            return redirect(cnct)
    else:
        return render(req,'contact.html')

def retrn(req):
    return redirect(instf)