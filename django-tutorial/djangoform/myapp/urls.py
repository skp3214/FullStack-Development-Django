from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form, name='form'),
    path('formadd/', views.formAdd, name='formadd'),
    path('form1/',views.form1),
    path('success/',views.success,name='success'),
    path('htmlform/',views.htmlForm),
    path('validform/',views.validateForm),
]
