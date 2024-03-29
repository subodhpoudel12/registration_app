# Generated by Django 4.2.8 on 2024-02-29 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationsInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('organizationCode', models.CharField(max_length=20, unique=True)),
                ('organizationName', models.CharField(max_length=20, unique=True)),
                ('organizationType', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('localLevel', models.CharField(max_length=20)),
                ('wardNo', models.IntegerField(default=1)),
                ('tole', models.CharField(max_length=20)),
                ('contactNo', models.IntegerField(default=0)),
                ('contactPerson', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StudentsInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=30)),
                ('fatherName', models.CharField(max_length=30)),
                ('guardianName', models.CharField(max_length=30)),
                ('guardianPhoneNo', models.IntegerField(default=0)),
                ('grade', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('rollNo', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('localLevel', models.CharField(max_length=20)),
                ('wardNo', models.IntegerField(default=0)),
                ('tole', models.CharField(max_length=20)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration_app.organizationsinfo')),
            ],
        ),
    ]
