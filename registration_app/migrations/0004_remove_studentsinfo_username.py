# Generated by Django 5.0.3 on 2024-03-15 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0003_alter_studentsinfo_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsinfo',
            name='userName',
        ),
    ]