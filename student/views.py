from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'student/student_dashboard.html')


def student_view_attendance(request):
    return render(request,'student/student_view_attendance.html')


def student_change_pass(request):
    return render(request,'student/student_change_pass.html')


def logout(request):
    return render(request,'index.html')
