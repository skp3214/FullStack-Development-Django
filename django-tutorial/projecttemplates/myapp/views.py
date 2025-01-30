from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request,'test.html')

def pass_data(request):
    details={'name':{
        'firstname':'Sachin',
        'lastname':'prajapati'
    }}
    return render(request,'data.html',details)

def classtask(request):
    details=[
        {'name':'ayush','marks':30,'age':20},
        {'name':'sachin','marks':45,'age':23},
        {'name':'sameer','marks':55,'age':24},
        {'name':'saif','marks':65,'age':25},
    ]
    return render(request,'multidata.html',{'details':details})