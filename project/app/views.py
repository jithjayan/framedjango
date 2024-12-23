from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student
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

def day(req,a):
    if a==1:
        return HttpResponse('Sunday')
    elif a==2:
        return HttpResponse('monday')
    elif a==3:
        return HttpResponse('Tuesday')
    elif a==4:
        return HttpResponse('wednesday')
    elif a==5:
        return HttpResponse('Thursday')
    elif a==6:
        return HttpResponse('Friday')
    elif a==7:
        return HttpResponse('saturday')
    else:
        return HttpResponse('invalid')
def bonus(request,a,b):
    if b>5:
        c=0.05*a
        return HttpResponse(c)
    else:
        return HttpResponse('no change')


def tax(req,a):
    if a>100000:
        b=a*15/100
        total=a+b
        return HttpResponse(total)
    elif a>50000 and a<=100000:
        b=a*10/100
        total=a+b
        return HttpResponse(total)
    else:
        b=a*5/100
        total=a+b
        return HttpResponse(total)
    
def bill(req,a):
    if a<100:
        return HttpResponse("Your unit price = 0")
    else:
        if a<200 and a>100:
            up=a-100
            ua=up*5
            return HttpResponse(ua)
        else:
            ui=a-200
            us=ui*10+500
            return HttpResponse(us)

def demo(req):
    
    b=[{'name':'awe','age':12},{'name':'dice','age':14},{'name':'eza','age':14}]
    return render(req,'demo.html',{'data':b})

users=[{'id':'1001','name':'awe','age':12,'email':'awe@gmail.com'},{'id':'1002','name':'dice','age':14,'email':'dice@gmail.com'},{'id':'1003','name':'eza','age':14,'email':'eza@gmail.com'}]
def display(req):
    return render(req,'display_usr.html',{'users':users})


def user_reg(req):
    if req.method=='POST':
        id=req.POST['id']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        users.append({'id':id,'name':name,'age':age,'email':email})
        return redirect(display)
    else:
        print(req.method)
        return redirect(display)

def edit_user(req,id):
    user=''
    for i in users:
        if i['id']==id:
            user=i
    if req.method=='POST':
        id=req.POST['id']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        user['id']=id
        user['name']=name
        user['age']=age
        user['email']=email
        return redirect(display)
    
    return render(req,'edit_user.html',{'user':user})

def delete_user(req,id):
    for i in users:
        if i['id']==id:
            users.remove(i)
    return redirect(display)

def index(req):
    return render(req,'index.html')

def display_std(req):
    data=student.objects.all()
    return render(req,'display_std.html',{'std':data})

def add_std(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        email1=req.POST['email']
        data=student.objects.create(roll_no=roll,name=name,age=age,email=email1)
        data.save()
        return redirect(display_std)
    else:
        return render(req,'add_std.html')

def edit_std(req,id):
    data=student.objects.get(pk=id)
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        email1=req.POST['email']
        student.objects.filter(pk=id).update(roll_no=roll,name=name,age=age,email=email1)
        return redirect(display_std)
    return render(req,'edit_std.html',{'data':data})

def delete_std(req,id):
    data=student.objects.get(pk=id)
    data.delete()
    return redirect(display_std)