"""
Database models for registration_app.
"""
from django.db import models

class OrganizationsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30, unique=True)
    organizationCode = models.CharField(max_length=20, unique=True)
    organizationName = models.CharField(max_length=20, unique=True)
    organizationType = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    localLevel = models.CharField(max_length=20)
    wardNo = models.IntegerField(default=1)
    tole = models.CharField(max_length=20)
    contactNo = models.IntegerField(default=0) 
    contactPerson = models.CharField(max_length=20)

class StudentsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=30, unique=True)
    organization = models.ForeignKey(OrganizationsInfo, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    fatherName= models.CharField(max_length=30)
    guardianName = models.CharField(max_length=30)
    guardianPhoneNo = models.IntegerField(default=0)
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    rollNo=models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    localLevel = models.CharField(max_length=20)
    wardNo = models.IntegerField(default=0)
    tole = models.CharField(max_length=20)
    
