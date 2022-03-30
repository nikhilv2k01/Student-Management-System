from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def add_teacher(request):
    return render(request,'add_teacher.html')

def teacher_list(request):
    return render(request,'teacher_list.html')

def add_attendance(request):
    return render(request,'add_attendance.html')

def view_attendance(request):
    return render(request,'view_attendance.html')

def teacher_attendance(request):
    return render(request,'teacher_attendance.html')

def add_student(request):
    return render(request,'add_student.html')

def student_fees(request):
    return render(request,'students_fees.html')

def student_list(request):
    return render(request,'student_list.html')

def logout(request):
    return render(request,'index.html')

