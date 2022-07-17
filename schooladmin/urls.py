from unicodedata import name
from . import views
from django.urls import path

app_name = 'school_admin'
urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('add-teacher', views.add_teacher, name="add_teacher"),
    path('teacher-list', views.teacher_list, name="teacher_list"),
    path('post-attendance', views.add_attendance, name="post_attendance"),
    path('view-attendance', views.view_attendance, name="view_attendance"),
    path('teacher-attendance', views.teacher_attendance, name="teacher_attendance"),
    path('add-student', views.add_student, name="add_student"),
    path('student-fees', views.student_fees, name="student_fees"),
    path('student-list', views.student_list, name="student_list"),
    path('view-class/<int:id>', views.view_class, name="view_class"),
    path('view-certificate/<int:id>', views.view_certificate, name="view_certificate"),
    path('teacher-edit',views.teacher_edit, name='teacher_edit'),
    path('logout', views.admin_logout, name="logout"),
    path('home', views.home, name="home"),

]
