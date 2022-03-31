from django.shortcuts import render

# Create your views here.

def common(request):
    return render(request,'common/index.html')
def login(request):
    return render(request,'common/admin_login.html')
def teacher_login(request):
    return render(request,'common/teacher_login.html')
def student_login(request):
    return render(request,'common/student_login.html')
