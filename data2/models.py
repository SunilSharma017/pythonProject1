from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    dob=models.DateField()
class OtherInformation(models.Model):
    city= models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    subjects=models.CharField(max_length=100)


