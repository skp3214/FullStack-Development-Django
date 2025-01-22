from django.urls import path,re_path
from . import views

urlpatterns = [
    path('hello/',views.message),
    path('message/',views.message1),
    path('items/',views.menuitems),
    path('menuitems/<str:item>/',views.menuitems1),
    path('add/<str:num1>/<str:num2>/',views.addtion),
    path('add/',views.queryAddition),
    path('op/',views.operation),
    re_path(r'^username/(?P<username>[a-zA-Z0-9\s()-_%]+)/$',views.usernameFun),
    re_path(r'^userid/(?P<userid>\w+)/$',views.userId),
    re_path(r'student/(?P<studentname>\w+)/(?P<studentid>\d{3})/$',views.moreParam),
    re_path(r'date/(?P<month>\d{3,4})/(?P<year>[0-9]*)',views.monthYear),
    
]
