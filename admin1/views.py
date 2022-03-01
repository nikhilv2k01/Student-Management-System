from django.shortcuts import render

# Create your views here.

def admin1(request):
    return render(request,'master.html')
def teacher(request):
    return render(request,'admin-teacher.html')
def student(request):
    return render(request,'admin-student.html')
def staff(request):
    return render(request,'admin-staff.html')
def report(request):
    return render(request,'admin-report.html')
def logout(request):
    return render(request,'index.html')

