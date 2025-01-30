from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.test),
    path('data/',views.pass_data),
    path('multidata/',views.classtask)
]

