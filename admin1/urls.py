from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [   
    
    path('add-teacher',views.add,name="add_teacher"),
    path('teacher-list',views.t_list,name="teacher_list"),
    path('post-attendance',views.p_attendance,name="post_attendance"),
    path('view-attendance',views.v_attendance,name="view_attendance"),
    path('teacher-attendance',views.t_attendance,name="teacher_attendance"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('add-student',views.a_student,name="add_student"),
    path('student-fees',views.s_fees,name="student_fees"),
    path('student-list',views.s_list,name="student_list"),
    path('log-out',views.logout,name="logout"),

]