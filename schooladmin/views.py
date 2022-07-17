import re
from django.shortcuts import render, redirect
from . models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings

import string
import random



# Create your views here.

@api_view(['GET'])
def home(request):
    message='congrats'
    return Response(message)


def dashboard(request):
    return render(request, 'schooladmin/dashboard.html')


def add_teacher(request):
    if request.method == 'POST':
        name = request.POST['name']
        salary = request.POST['salary']
        gender = request.POST['gender']
        date_of_birth = request.POST['dateofbirth']
        teacher_class = request.POST['class']
        course = request.POST['course']
        contact_number = request.POST['number']
        email = request.POST['email']
        address = request.POST['address']
        post_code = request.POST['postcode']
        city = request.POST['city']
        certificate = request.FILES['certificate']
        teacher = AddTeachers(first_name=name, salary=salary,
                              gender=gender, date_of_birth=date_of_birth, teacher_class=teacher_class, course=course, contact_number=contact_number, email=email, address=address, post_code=post_code, city=city, certificate=certificate)
        teacher.save()

    return render(request, 'schooladmin/add_teacher.html')


def teacher_list(request):

    teacher_list = AddTeachers.objects.all()
    if request.method == 'POST':
        close_btn = request.POST['close_btn']
        teacher = AddTeachers.objects.get(id=close_btn)
        teacher.delete()

    return render(request, 'schooladmin/teacher_list.html', {'teacher': teacher_list, })


def add_attendance(request):
    add_attendance = AddTeachers.objects.all()
    return render(request, 'schooladmin/add_attendance.html', {'add_attendance': add_attendance, })


def view_attendance(request):

    return render(request, 'schooladmin/view_attendance.html')


def teacher_attendance(request):
    return render(request, 'schooladmin/teacher_attendance.html')


def add_student(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        date_of_birth = request.POST['dateofbirth']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        gender = request.POST['gender']
        contact_number = request.POST['contact_number']
        student_class = request.POST['class']
        course = request.POST['course']
        email = request.POST['email']
        address = request.POST['address']
        fees = request.POST['fees']
        certificate = request.FILES['certificate']

        student = AddStudent(student_name=student_name, date_of_birth=date_of_birth, father_name=father_name,
                             mother_name=mother_name, gender=gender, contact_number=contact_number, student_class=student_class, course=course, email=email, address=address, fees=fees, certificate=certificate)

        student.save()
        # initializing size of string 
        N = 7
        # generating random strings 
        res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))

        to = email
        subject = 'School user id and password'
        msg = ""
        send_mail(subject, msg, settings.EMAIL_HOST_USER, [to, ])
    return redirect('customer:cust_home')


    return render(request, 'schooladmin/add_student.html')


def student_fees(request):
    return render(request, 'schooladmin/students_fees.html')


def student_list(request):
    student_list = AddStudent.objects.all()

    return render(request, 'schooladmin/student_list.html', {'student': student_list, })


def view_class(request, id):
    view_class = AddTeachers.objects.get(id=id)
    
    if request.method == 'POST':
        close_btn = request.POST['view_class_btn']
        teacher = AddTeachers.objects.get(id=close_btn)
        teacher.delete()
        return redirect('school_admin:teacher_list')
    return render(request, 'schooladmin/view_class.html', {'view_class': view_class, })


def view_certificate(request, id):
    view_certificate = AddTeachers.objects.get(id=id)

    if request.method == 'POST':
        close_btn = request.POST['view_certificate_btn']
        teacher = AddTeachers.objects.get(id=close_btn)
        teacher.delete()
        return redirect('school_admin:teacher_list')
    return render(request, 'schooladmin/view_certificate.html', {'view_certificate': view_certificate, })


def teacher_edit(request):
    return render(request, 'schooladmin/teacher_edit.html')


def admin_logout(request):
    del request.session['admin_id']
    request.session.flush()
    return redirect('common:common')
