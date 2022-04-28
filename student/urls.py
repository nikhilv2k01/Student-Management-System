from unicodedata import name
from . import views
from django.urls import path

app_name='student'
urlpatterns = [   
    path('dashboard',views.dashboard,name="dashboard"),
    path('view-attendance',views.student_view_attendance,name="view_attendance"),
    path('change-pass',views.student_change_pass,name="change_pass"),
    path('logout',views.logout,name="logout"),

]