from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogform,name='blogform'),
    path('bloglist/',views.bloglist,name='bloglist')
]