from django.urls import path
from . import views
urlpatterns = [
    path('', views.setCookie, name='setcookie'),
    path('gc/', views.getCookie, name='getcookie'),
    path('dc/', views.deleteCookie, name='deletecookie'),
    path('theme/', views.setLightDarkTheme, name='setLightDarkTheme'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('lvp/', views.lastVisitedPage, name='lastVisitedPage'),
    path('page/', views.pageNow, name='pageNow'),
]