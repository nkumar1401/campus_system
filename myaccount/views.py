from django.shortcuts import render ,redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User

from student.models import *
# Create your views here.
def signup(request):
    if request.method=='POST':
        fn=request.POST.get('fn')
        ln=request.POST.get('ln')
        un=request.POST.get('un')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1==pass2:
            if User.objects.filter(username=un).exists():
             messages.error(request,'user name already exists')
             return redirect('signup')
                
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'already have email')
                    return redirect('signup')
                else:
                    user=User.objects.create_user(username=un,password=pass1,first_name=fn,last_name=ln)
                    user.save()
                    messages.info(request,'sign up successfully')
                    return redirect('login')
            
        
        else:
            messages.error(request,'password not match')
            return redirect('signup')

    return render (request,'myaccount/signup.html')
def login(request):
    if request.method=='POST':
        un=request.POST.get('un')
        password=request.POST.get('pass')
        user=auth.authenticate(username=un,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'login successfully')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credential')
            return redirect('login')
    return render (request,'myaccount/login.html')

# def dashboard(request):
#     data=Student_details.objects.all()
#     context={
#         'students':data
#     }
#     return render (request,'myaccount/dashboard.html',context)  
def dashboard(request):
    data=Enroll_details.objects.all()
    context={
        'students':data
    }
    return render (request,'myaccount/dashboard.html',context)  
def logout(request):
    auth.logout(request)
    return redirect ('login') 

def singlestudent(request,reg_id):
    student=Enroll_details.objects.get(reg_id=reg_id)
    context={
        'student':student
    }
    if request.method=='POST':
        name=request.POST.get('name')
        city=request.POST.get('city')
        email=request.POST.get('email')
        degree=request.POST.get('degree')
        percentage=request.POST.get('percentage')
        courses=request.POST.get('courses')
        date=request.POST.get('date')
        fee=request.POST.get('fee')
        student=Enroll_details.objects.get(reg_id=reg_id)
        student.name=name
        student.city=city
        student.email=email
        student.degree=degree
        student.percentage=percentage
        student.courses=courses
        student.fee=fee
        student.save()
        return redirect('dashboard')

    return render(request,'myaccount/singlestudent.html',context) 

def delete(request,reg_id):
    student=Enroll_details.objects.get(reg_id=reg_id)
    student.delete()

    return redirect('dashboard')