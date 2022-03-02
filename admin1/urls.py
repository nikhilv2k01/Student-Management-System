from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [   
    path('adm',views.admin1,name="home"),
    path('add',views.add,name="add_teacher"),
    path('del',views.delete,name="delete_teacher"),
    path('upt',views.update,name="update_teacher"),
    path('src',views.search,name="search_teacher"),
    path('atd',views.t_attendance,name="teacher_attendance"),
    path('lgt',views.logout,name="logout"),

]