from django.db import models

from django.db import models
class applicant(models.Model):
    app=models.CharField(max_length=255)
class student(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    guardianfirstname=models.CharField(max_length=255)
    guardianlastname=models.CharField(max_length=255)
    age=models.CharField(max_length=100)
    sex=models.CharField(max_length=1)
    mobilenumber=models.CharField(max_length=100)
    entrynumber=models.CharField(max_length=12)
    department=models.CharField(max_length=5)
    hostel=models.CharField(max_length=20)
    roomnumber=models.CharField(max_length=10)
    emergencynumber=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    swim=models.CharField(max_length=1)
    # slot1=models.CharField(max_length=4)
    # slot2=models.CharField(max_length=4)
class faculty(models.Model):
    Name=models.CharField(max_length=255)
    Designation=models.CharField(max_length=255)
    Family=models.CharField(max_length=255)
    Relation=models.CharField(max_length=255)
    age=models.CharField(max_length=100)
    sex=models.CharField(max_length=1)
    mobilenumber=models.CharField(max_length=100)
    EmpCode=models.CharField(max_length=12)
    department=models.CharField(max_length=5)
    
    
    emergencynumber=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    swim=models.CharField(max_length=1)