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

def studentData(request):
    details = {
    'complete_details':[
    {'name':'Ashish','marks':30,'age':20,'status':'fail'},
    {'name':'Manoj','marks':78,'age':19,'status':'pass'},
    {'name':'Aditi','marks':67,'age':21,'status':'pass'},
    {'name':'Ujjawal','marks':89,'age':22,'status':'pass'},
    {'name':'Raja','marks':32,'age':21,'status':'fail'},
    ]
    }
    return render(request,'student.html',details)

def linkTest(request):
    
    return render(request,'linktest.html')

def foodDetails(request, itemname):
    foodmenu = [
        {'itemname': 'biryani', 'price': 100, 'GST': 12,'size':'large'},
        {'itemname': 'juice', 'price': 100, 'GST': 18,'size':'small'},
        {'itemname': 'coffee', 'price': 50, 'GST': 5,'size':'medium'},
        {'itemname': 'tea', 'price': 150, 'GST': 10,'size':'large'},
    ]
    data = {}
    for item in foodmenu:
        if itemname == item['itemname']:
            data = item
            break
    
    return render(request, 'fooditem.html', {'data': foodmenu,'itemname':itemname})
    