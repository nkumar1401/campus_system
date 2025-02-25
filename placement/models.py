from django.db import models

# Create your models here.
class Placed_student(models.Model):
    photo=models.ImageField(upload_to='photo/%Y/%m/%d/')
    name=models.CharField(max_length=50)
    company=models.CharField(max_length=100)
    location=models.CharField(max_length=20)
    package=models.FloatField()