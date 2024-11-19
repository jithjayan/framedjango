from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.models import User
import os
from django.contrib import messages

# from django.contrib.auth.models import User
# Create your views here.
def ad_login(req):
    if 'shop' in req.session:
         return redirect(ad_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['paswd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['shop']=uname
                return redirect(ad_home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"Invalid uname or password")
            return redirect(login)

    else:
        return render(req,'login.html')
        
def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['paswd']
        try:
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(ad_login)
        except:
            messages.warning(req,"Email already exist")
            return redirect(register)
    else:
        return render(req,'user/register.html')
    
def user_home(req):
    if 'user' in req.session:
        # data=Galleryvault.objects.all()
        user=User.objects.get(username=req.session['user'])
        files=Galleryvault.objects.filter(user=user)
        return render(req,'user/home.html',{'Files':files})
    else:
        return redirect(login)
    
def add_file(req):
    #  if 'shop' in req.session:
          
        if req.method=='POST':
            name=req.POST['name']
            file=req.FILES['file']
            data=Galleryvault.objects.create(name=name,file=file)
            data.save()
            return redirect(user_home)
            
        else:
            return render(req,'user/add_file.html')
    #  else:
    #      return redirect(ad_login)
def user_logout(req):
        req.session.flush()
        logout(req)
        return redirect(ad_login)
def ad_home(req):
    return render(req,'homep.html')

def view_pro(req,pid):
    data=Galleryvault.objects.get(pk=pid)
    return render(req,'user/view_file.html',{'data':data})

def delete_file(req,pid):
    data=Galleryvault.objects.get(pk=pid)
    url=data.file.url
    og_path=url.split('/')[-1]
    os.remove('media/'+og_path)
    data.delete()
    print(og_path)
    return redirect(user_home)