from django.shortcuts import render ,redirect
from placement.models import Placed_student
from student.models import *
from django.contrib import messages


# Create your views here.
def home(request):
    return render (request,'student/home.html')
def aws(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile_no=request.POST.get('mobile')
        course=request.POST.get('course')
        qualification=request.POST.get('qualification')
        year_of_passing=request.POST.get('year')
        date=request.POST.get('date')
        data=Callback(name=name,mobile_no=mobile_no,qualification=qualification,course=course,year_of_passing=year_of_passing,date=date)
        data.save()
        messages.error(request,'We will connect you as soon as posssible')
        return redirect('home') 
    return render (request,'student/aws.html')
def java(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile_no=request.POST.get('mobile')
        course=request.POST.get('course')
        qualification=request.POST.get('qualification')
        year_of_passing=request.POST.get('year')
        date=request.POST.get('date')
        data=Callback(name=name,mobile_no=mobile_no,qualification=qualification,course=course,year_of_passing=year_of_passing,date=date)
        data.save()
        messages.error(request,'We will connect you as soon as posssible')
        return redirect('home') 
    return render (request,'student/java.html')
# def python(request):
#     return render (request,'student/python.html')
def registration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')  
        city=request.POST.get('city')
        degree=request.POST.get('degree')
        percentage=request.POST.get('percentage')
        courses=request.POST.get('courses')
        fee=request.POST.get('fee')
        data=Student_details(name=name,email=email,city=city,degree=degree,percentage=percentage,courses=courses,fee=fee)
        data.save()
        messages.error(request,'erollment successfully')
        return redirect('home')
    
    return render (request,'student/registration.html')

import time
import logging
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from student.models import Enroll_details

logger = logging.getLogger(__name__)  # Logger for tracking API time

def enroll(request):
    start_time = time.time()  # Start timer    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        degree = request.POST.get('degree')
        percentage = request.POST.get('percentage')
        courses = request.POST.get('courses')
        fee = request.POST.get('fee')
        date = request.POST.get('date')

        data = Enroll_details(name=name, email=email, city=city, degree=degree, 
                              percentage=percentage, courses=courses, fee=fee, date=date)
        data.save()
        messages.error(request, 'Enrollment successfully')
        response = redirect('home')  # Response after saving data

    else:
        response = render(request, 'student/enroll.html')

    end_time = time.time()  # End timer
    duration = (end_time - start_time) * 1000  # Convert to milliseconds

    logger.info(f"API: enroll | Method: {request.method} | Time Taken: {duration:.2f} ms")

    return response



logger = logging.getLogger(__name__)  # Define logger

def aboutus(request):
    start_time = time.time()  # Start timer

    response = render(request, 'student/aboutus.html')  # API response

    end_time = time.time()  # End timer
    duration = (end_time - start_time) * 1000  # Convert to milliseconds

    logger.info(f"API: aboutus | Method: {request.method} | Time Taken: {duration:.2f} ms")
    
    return response


# def enroll(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')  
#         city=request.POST.get('city')
#         degree=request.POST.get('degree')
#         percentage=request.POST.get('percentage')
#         courses=request.POST.get('courses')
#         fee=request.POST.get('fee')
#         date=request.POST.get('date')
#         data=Enroll_details(name=name,email=email,city=city,degree=degree,percentage=percentage,courses=courses,fee=fee,date=date)
#         data.save()
#         messages.error(request,'erollment successfully')
#         return redirect('home') 
       
#     return render (request,'student/enroll.html')
    

def python(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile_no=request.POST.get('mobile')
        course=request.POST.get('course')
        qualification=request.POST.get('qualification')
        year_of_passing=request.POST.get('year')
        date=request.POST.get('date')
        data=Callback(name=name,mobile_no=mobile_no,qualification=qualification,course=course,year_of_passing=year_of_passing,date=date)
        data.save()
        messages.error(request,'We will connect you as soon as posssible')
        return redirect('home') 
       
    return render (request,'student/python.html')


# def aboutus(request):
#     return render (request,'student/aboutus.html')
def placement(request):
    students=Placed_student.objects.all()
    context={
        'student':students
    }
    return render (request,'student/placement.html',context)
# def learnpy(request):
#     return render(request,'student/learnpy.html')
# def learnjava(request):
#     return render(request,'student/learnjava.html')
# def learnaws(request):
#     return render(request,'student/learnaws.html')
# def callback(request):
#     return render(request,'student/callback.html')
