from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def shop_login(req):

    if 'shop' in req.session:
         return redirect(shop_home)
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
                return redirect(shop_home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"Invalid uname or password")
            return redirect(shop_login)

    else:
        return render(req,'login.html')
    
def shop_logout(req):
        req.session.flush()
        logout(req)
        return redirect(shop_login)
    
def shop_home(req):
    if 'shop' in req.session:
        data=product.objects.all()[::-1]
        return render(req,'shop/home.html',{'products':data})
    else:
         return redirect(shop_login)

def add_product(req):
     if 'shop' in req.session:
          
        if req.method=='POST':
            id=req.POST['pro_id']
            name=req.POST['name']
            price=req.POST['price']
            offer_price=req.POST['offer_price']
            img=req.FILES['img']
            disp=req.POST['disp']
            data=product.objects.create(pro_id=id,name=name,price=price,offer_price=offer_price,img=img,disp=disp)
            data.save()
            return redirect(shop_home)
            
        else:
            return render(req,'shop/add_product.html')
     else:
         return redirect(shop_login)

def edit_product(req,pid):
    if 'shop' in req.session:
          
        if req.method=='POST':
            id=req.POST['pro_id']
            name=req.POST['name']
            price=req.POST['price']
            offer_price=req.POST['offer_price']
            img=req.FILES.get('img')
            disp=req.POST['disp']
            if img:
                product.objects.filter(pk=pid).update(pro_id=id,name=name,price=price,offer_price=offer_price,img=img,disp=disp)
            else:
                 product.objects.filter(pk=pid).update(pro_id=id,name=name,price=price,offer_price=offer_price,disp=disp)
            return redirect(shop_home)
            
        else:
            data=product.objects.get(pk=pid)
            return render(req,'shop/edit.html',{'product':data})
    else:
        return redirect(shop_login)
    

def delete_product(req,pid):
    data=product.objects.get(pk=pid)
    url=data.img.url
    og_path=url.split('/')[-1]
    os.remove('media/'+og_path)
    data.delete()
    print(og_path)
    return redirect(shop_home)

def bookings(req):
    buy=Buy.objects.all()[::-1]
    return render(req,'shop/bookings.html',{'buy':buy})




# -----------------USER-------------------
def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['paswd']
        try:
            send_mail('user registration', 'account created', settings.EMAIL_HOST_USER, [email])
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(shop_login)
        except:
            messages.warning(req,"Email not valid")
            return redirect(register)
    else:
        return render(req,'user/register.html')


def user_home(req):
    if 'user' in req.session:
        data=product.objects.all()
        return render(req,'user/home.html',{'data':data})
    else:
        return redirect(shop_login)
    
def view_pro(req,pid):
    data=product.objects.get(pk=pid)
    return render(req,'user/view_pro.html',{'data':data})

def add_to_cart(req,pid):
    prdct=product.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    data=cart.objects.create(user=user,product=prdct)
    data.save()
    return redirect(view_cart)

def view_cart(req):
    user=User.objects.get(username=req.session['user'])
    cart_dtls=cart.objects.filter(user=user)
    return render(req,'user/cart.html',{'cart_dtls':cart_dtls})

def delete_cart(req,id):
    cartt=cart.objects.get(pk=id)
    cartt.delete()
    return redirect(view_cart)

def user_buy(req,cid):
    user=User.objects.get(username=req.session['user'])
    cartt=cart.objects.get(pk=cid)
    product=cartt.product
    price=cartt.product.offer_price
    buy=Buy.objects.create(user=user,product=product,price=price)
    buy.save()
    # cart.delete()
    return redirect(view_cart)

def user_buy1(req,pid):
    user=User.objects.get(username=req.session['user'])
    prdct=product.objects.get(pk=pid)
    price=prdct.offer_price
    buy=Buy.objects.create(user=user,prdct=prdct,price=price)
    buy.save()
    return redirect(user_home)
    

def user_bookings(req):
    user=User.objects.get(username=req.session['user'])
    buy=Buy.objects.filter(user=user)[::-1]
    return render(req,'user/bookings.html',{'buy':buy})
