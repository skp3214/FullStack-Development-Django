from django.shortcuts import render,redirect

# Create your views here.
from .models import BlogPost
from .forms import BlogPostForm

def blogform(request):
    form=BlogPostForm()
    if request.method=='POST':
        form=BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bloglist')
    return render(request,'blogform.html',{'form':form})

def bloglist(request):
    blogs=BlogPost.objects.all()
    return render(request,'allblogs.html',{'blogs':blogs})