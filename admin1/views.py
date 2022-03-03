from django.shortcuts import render

# Create your views here.


def add(request):
    return render(request,'add_teacher.html')
def delete(request):
    return render(request,'delete_teacher.html')
def update(request):
    return render(request,'update_teacher.html')
def search(request):
    return render(request,'search_teacher.html')
def t_attendance(request):
    return render(request,'teacher_attendance.html')
def dashboard(request):
    return render(request,'dashboard.html')
def a_student(request):
    return render(request,'add_student.html')
def s_fees(request):
    return render(request,'students_fees.html')
def logout(request):
    return render(request,'index.html')
