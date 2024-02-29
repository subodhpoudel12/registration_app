from rest_framework import serializers
from .models import OrganizationsInfo, StudentsInfo

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationsInfo
        fields = ['id', 'email', 'organizationCode', 'organizationName', 'organizationType', 'province', 'district', 'localLevel', 'wardNo', 'tole', 'contactNo', 'contactPerson']

class StudentSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(queryset=OrganizationsInfo.objects.all())  # or use StringRelatedField if you want to represent it as a string
    class Meta:
        model = StudentsInfo
        fields = ['id', 'fullName', 'organization', 'email', 'fatherName', 'guardianName', 'guardianPhoneNo', 'province', 'district', 'localLevel', 'wardNo', 'tole', 'grade', 'section', 'rollNo']
