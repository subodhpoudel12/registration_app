# Generated by Django 5.0.3 on 2024-03-15 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0004_remove_studentsinfo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsinfo',
            name='userName',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
