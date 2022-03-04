from django.shortcuts import render

# Create your views here.


def add(request):
    return render(request,'add_teacher.html')
def t_list(request):
    return render(request,'teacher_list.html')
def p_attendance(request):
    return render(request,'post_attendance.html')
def v_attendance(request):
    return render(request,'view_attendance.html')
def t_attendance(request):
    return render(request,'teacher_attendance.html')
def dashboard(request):
    return render(request,'dashboard.html')
def a_student(request):
    return render(request,'add_student.html')
def s_fees(request):
    return render(request,'students_fees.html')
def s_list(request):
    return render(request,'student_list.html')
def logout(request):
    return render(request,'index.html')
