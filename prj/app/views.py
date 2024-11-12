from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
# Create your views here.
def shop_login(req):
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['pswd']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                req.session['shop']=uname
                return redirect(shop_home)
            # else:
            #     messages.warning(req,"Invalid uname or password")
            #     return redirect(shop_login)
        else:
            return render(req,'login.html')   

def shop_logout(req):
        req.session.flush()
        logout(req)
        return redirect(shop_login)

def shop_home(req):
    # if 'shop' in req.session:
        data=plants.objects.all()[::-1]
        return render(req,'shop/shop_home.html',{'plants':data})
    # else:
    #      return redirect(shop_login)

def add_plants(req):
    #  if 'shop' in req.session:
          
        if req.method=='POST':
            id=req.POST['p_id']
            name=req.POST['name']
            type=req.POST['p_type']
            price=req.POST['price']
            img=req.FILES['img']
            stock=req.POST['stock']
            disp=req.POST['disp']
            data=plants.objects.create(p_id=id,name=name,p_type=type,price=price,img=img,stock=stock,disp=disp)
            data.save()
            return redirect(shop_home)
            
        else:
            return render(req,'shop/add_plants.html')
    #  else:
        #  return redirect(shop_login)

def edit_plants(req,pid):
    # if 'shop' in req.session:
          
        if req.method=='POST':
            id=req.POST['p_id']
            name=req.POST['name']
            type=req.POST['p_type']
            price=req.POST['price']
            img=req.FILES.get('img')
            stock=req.POST['stock']
            disp=req.POST['disp']
            if img:
                plants.objects.filter(pk=pid).update(p_id=id,name=name,p_type=type,price=price,stock=stock,disp=disp)
                data=plants.objects.get(pk=pid)
                data.img=img
                data.save()
            else:
                 plants.objects.filter(pk=pid).update(p_id=id,name=name,p_type=type,price=price,stock=stock,disp=disp)
            return redirect(shop_home)
            
        else:
            data=plants.objects.get(pk=pid)
            return render(req,'shop/edit_plants.html',{'plants':data})
    # else:
    #     return redirect(shop_login)      


def delete_plants(req,pid):
    data=plants.objects.get(pk=pid)
    url=data.img.url
    og_path=url.split('/')[-1]
    os.remove('media/'+og_path)
    data.delete()
    print(og_path)
    return redirect(shop_home)


def search_plants(req):
    pass
     
     