from django.urls import path

from . import views

urlpatterns = [
    path('', views.signupform, name='signupform'),
    path('delete/<int:id>', views.delete_user, name='delete_user'),
    path('update/<int:id>', views.update_user, name='update_user')
]