from django.shortcuts import render,redirect
from . models import AdminLogin

# Create your views here.

def common(request):
    return render(request,'common/index.html')
def login(request):
    msg=''
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user_exist=AdminLogin.objects.filter(username=username,password=password).exists()
        if user_exist:
            return redirect('school_admin:dashboard')
        else:
            msg='invalid username or password !'

    
    return render(request,'common/admin_login.html',{'err_msg':msg,})

def teacher_login(request):
    msg=''
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user_exist=AdminLogin.objects.filter(username=username,password=password).exists()
        if user_exist:
            return redirect('school_admin:dashboard')
        else:
            msg='invalid username or password !'
    return render(request,'common/teacher_login.html')
def student_login(request):
    return render(request,'common/student_login.html')
