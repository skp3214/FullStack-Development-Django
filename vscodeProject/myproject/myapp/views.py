from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
# Create your views here.

def home(request):
    return HttpResponse("hello, world! This is my home page.")

def book(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})