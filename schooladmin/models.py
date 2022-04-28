from re import M
from statistics import mode
from django.db import models

# Create your models here.
# class AddTeacher:

class AddTeachers(models.Model):
    first_name=models.CharField(max_length=20)
    salary=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    date_of_birth=models.CharField(max_length=10)
    teacher_class=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    contact_number=models.BigIntegerField()
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=20)
    post_code=models.IntegerField()
    city=models.CharField(max_length=20)
    certificate=models.ImageField(upload_to='product/')

    class Meta:
        db_table='add_teacher'


class AddStudent(models.Model):
    student_name=models.CharField(max_length=20)
    date_of_birth=models.CharField(max_length=100)
    father_name=models.CharField(max_length=20)
    mother_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    contact_number=models.BigIntegerField()
    student_class=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    fees=models.BigIntegerField()
    certificate=models.ImageField(upload_to='product/')

    class Meta:
        db_table='add_student'

