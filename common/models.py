from urllib import request
from django.db import models

# Create your models here.


class AdminLogin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'admin_login'


class TeacherLogin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'teacher_login'


class StudentLogin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'student_login'
