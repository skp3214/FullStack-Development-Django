from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.test),
    path('data/',views.pass_data),
    path('multidata/',views.classtask),
    path('student/',views.studentData,name='student_details'),
    path('test/',views.linkTest),
    path('foodmenu/<str:itemname>',views.foodDetails)
]

