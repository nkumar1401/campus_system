from django.db import models


# Create your models here.
class Student_details(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.EmailField(max_length=100 ,null=True)
    degree=models.CharField(max_length=100,null=True)
    fee=models.IntegerField(null=True)
    courses=models.CharField(max_length=100,null=True)
    percentage=models.FloatField(null=True)


class Enroll_details(models.Model):
    reg_id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.EmailField(max_length=100 )
    degree=models.CharField(max_length=100)
    fee=models.IntegerField()
    courses=models.CharField(max_length=100)
    percentage=models.FloatField()
    date=models.DateField(null=True)

class Callback(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100) 
    year_of_passing=models.IntegerField()
    qualification=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=10)
    date=models.DateField(null=True)

    
