from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [   
    path('adm',views.admin1,name="home"),
    path('tch',views.teacher,name="teacher"),
    path('std',views.student,name="student"),
    path('stf',views.staff,name="staff"),
    path('rpt',views.report,name="report"),
    path('lgt',views.logout,name="logout"),

]