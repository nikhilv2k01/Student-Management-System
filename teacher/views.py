from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'teacher/dashboard.html')

def exam(request):
    return render(request,'teacher/exam.html')

def student_list(request):
    return render(request,'teacher/student_list.html')

def time_table(request):
    return render(request,'teacher/timetable.html')


