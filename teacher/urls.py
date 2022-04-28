from unicodedata import name
from . import views
from django.urls import path

app_name='teacher'
urlpatterns = [   
    path('dashboard',views.dashboard,name="dashboard"),
    path('exam',views.exam,name="exam"),
    path('studentlist',views.student_list,name="student_list"),
    path('timetable',views.time_table,name="timetable"),
    path('changepass',views.change_pass,name="change_pass"),
   
]