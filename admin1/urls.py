from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [   
    path('adm',views.Admin1),
    path('teacher',views.Teacher)
]