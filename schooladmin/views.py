import re
from django.shortcuts import render, redirect
from . models import *

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


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

    return render(request, 'add_teacher.html')


def teacher_list(request):

    teacher_list=AddTeachers.objects.all()
    


    if request.method=='POST':
        close_btn=request.POST['close_btn']
        teacher=AddTeachers.objects.get(id=close_btn)
        teacher.delete()


    return render(request, 'teacher_list.html',{'teacher':teacher_list,})


def add_attendance(request):
    return render(request, 'add_attendance.html')


def view_attendance(request):
    return render(request, 'view_attendance.html')


def teacher_attendance(request):
    return render(request, 'teacher_attendance.html')


def add_student(request):
    return render(request, 'add_student.html')


def student_fees(request):
    return render(request, 'students_fees.html')


def student_list(request):
    return render(request, 'student_list.html')


def view_class(request,id):
    view_class=AddTeachers.objects.get(id=id)

    if request.method=='POST':
        close_btn=request.POST['view_class_btn']
        teacher=AddTeachers.objects.get(id=close_btn)
        teacher.delete()
        return redirect('school_admin:teacher_list')
    return render(request, 'view_class.html',{'view_class':view_class,})


def view_certificate(request,id):
    view_certificate=AddTeachers.objects.get(id=id)
   
    if request.method=='POST':
        close_btn=request.POST['view_certificate_btn']
        teacher=AddTeachers.objects.get(id=close_btn)
        teacher.delete()
        return redirect('school_admin:teacher_list')
    return render(request,'view_certificate.html',{'view_certificate':view_certificate,})


def teacher_edit(request):
    return render(request, 'teacher_edit.html')


def admin_logout(request):
    request.session.flush()
    return redirect('common:common')
