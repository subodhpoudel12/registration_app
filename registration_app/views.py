from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework.response import Response

class OrganizationView(APIView):
    def get(self, request): 
        output = [{"id":output.id,
                   "email":output.email,
                   "organizationCode":output.organizationCode,
                   "organizationName":output.organizationName,
                   "organizationType":output.organizationType,
                   "province":output.province,
                   "district":output.district,
                   "localLevel":output.localLevel,
                   "wardNo":output.wardNo,
                   "tole":output.tole,
                   "contactNo":output.contactNo,
                   "contactPerson":output.contactPerson,

                   }
                   for output in OrganizationsInfo.objects.all()]
        return Response(output)
    def post(self, request):
        serializer=OrganizationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
         serializer.save()
        return Response(serializer.data)

class StudentView(APIView):
    def get(self, request): 
        output = [{
            "id": output.id,
            "email": output.email,
            "fullName": output.fullName,
            "organization": {
                "id": output.organization.id,
                "email": output.organization.email,
                "organizationCode": output.organization.organizationCode,
                "organizationName": output.organization.organizationName,
                "organizationType": output.organization.organizationType,
                "province": output.organization.province,
                "district": output.organization.district,
                "localLevel": output.organization.localLevel,
                "wardNo": output.organization.wardNo,
                "tole": output.organization.tole,
                "contactNo": output.organization.contactNo,
                "contactPerson": output.organization.contactPerson,
            },
            "fatherName": output.fatherName,
            "province": output.province,
            "district": output.district,
            "localLevel": output.localLevel,
            "wardNo": output.wardNo,
            "tole": output.tole,
            "guardianName": output.guardianName,
            "guardianPhoneNo": output.guardianPhoneNo,
            "grade": output.grade,
            "section": output.section,
            "rollNo": output.rollNo
        } for output in StudentsInfo.objects.all()]
        return Response(output)

    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


def index_view(request):
    return render(request, 'registration_app/register.html')
