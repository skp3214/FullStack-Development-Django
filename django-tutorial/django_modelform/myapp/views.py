from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm

def signupform(request):
    account_created=False
    form = UserForm()
    user = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            account_created=True
            return render(request,'signup.html',{'account_created':account_created,'form':form,'users':user})
    return render(request,'signup.html',{'form':form,'users':user})

def update_user(request,id):
    user = User.objects.get(pk=id)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('signupform')
    return render(request,'update.html',{'form':form})

def delete_user(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('signupform')