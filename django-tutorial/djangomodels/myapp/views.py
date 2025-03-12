from django.shortcuts import render,redirect
# Create your views here.
from .models import User

def signupform(request):
    account_created=False
    user = User.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create(username=username,email=email,password=password)
        account_created=True
        return render(request,'signup.html',{'account_created':account_created,'users':user})
    return render(request,'signup.html',{'users':user})

def delete_user(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    
    return redirect('signupform')

def update_user(request,id):
    user = User.objects.get(pk=id)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()
        return redirect('signupform')
    return render(request,'update.html',{'user':user})