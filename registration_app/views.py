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
from rest_framework import status


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
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from django.shortcuts import render, redirect
# from .models import OrganizationsInfo
# # from .forms import OrganizationForm  # Import your form if you have one

# def register_organization(request):
#     if request.method == 'POST':
#         # Create a form instance and populate it with data from the request
#         form = OrganizationForm(request.POST)
#         if form.is_valid():
#             # If the form is valid, save the data to the database
#             form.save()
#             # Redirect to a success page or wherever you want
#             return redirect('success_page')  # Change 'success_page' to the name of your success page URL
#     else:
#         # If a GET (or any other method) we'll create a blank form
#         form = OrganizationForm()
#     return render(request, 'register.html', {'form': form})
def index_view(request):
    return render(request, 'registration_app/register.html')

# class OrganizationView(APIView):
#     def post(self, request):
#         serializer = OrganizationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)