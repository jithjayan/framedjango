from django.shortcuts import render,redirect
from .models import student
from .forms import *
# Create your views here.
def user_def_form(req):
    if req.method=='POST':
        form1=user_form(req.POST)
        if form1.is_valid():
            roll=form1.cleaned_data['roll_number']
            name=form1.cleaned_data['name']
            age=form1.cleaned_data['age']
            email=form1.cleaned_data['email']
            data=student.objects. create(roll_no=roll,name=name,age=age,email=email)
            data.save()

    form=user_form()
    return render(req,'user_form.html',{'form':form})


def modelform_fun(req):
    if req.method=='POST':
        form1=model_form(req.POST)
        if form1.is_valid():
            form1.save()
        return redirect(modelform_fun)
    else:
        form=model_form()
        return render(req,'model_form.html',{'form':form})
    


