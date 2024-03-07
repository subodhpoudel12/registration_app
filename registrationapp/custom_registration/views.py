# serializers.py
from rest_framework import serializers
from .models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Organization
from .serializers import OrganizationSerializer

@api_view(['GET', 'POST'])
def organizations_list(request):
    if request.method == 'GET':
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def organization_detail(request, organization_id):
    try:
        organization = Organization.objects.get(pk=organization_id)
    except Organization.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrganizationSerializer(organization, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        organization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Separate user authentication views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Assuming 'home' is a valid URL name
        else:
            messages.error(request, "Invalid Login")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')  # Assuming 'login' is a valid URL name

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "User Created Successfully")
            return redirect('register_organization')  # Assuming 'register_organization' is a valid URL name
        else:
            messages.error(request, "Email or Username Already Exists")
    return render(request, 'register.html')
