from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.message),
    path('message/',views.message1),
    path('items/',views.menuitems),
    path('menuitems/<str:item>/',views.menuitems1),
    path('add/<str:num1>/<str:num2>/',views.addtion),
    path('add/',views.queryAddition),
    path('op/',views.operation)
]
