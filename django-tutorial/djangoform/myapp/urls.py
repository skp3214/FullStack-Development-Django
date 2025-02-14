from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form, name='form'),
    path('formadd/', views.formAdd, name='formadd'),
]
