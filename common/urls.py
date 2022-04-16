from unicodedata import name
from . import views
from django.urls import path

app_name='common'
urlpatterns = [   
    path('',views.common,name="common"),
    path('admlogin',views.login,name="admin_login"),
    path('teacherlogin',views.teacher_login,name="teacher_login"),
    path('studentlogin',views.student_login,name="student_login"),
]