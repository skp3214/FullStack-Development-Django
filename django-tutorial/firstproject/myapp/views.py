from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def message(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def message1(request):
    item="pizza"
    return HttpResponse(f'''<h1 style=color:red> hello</h1>
                        brothr, i like  {item}
                        ''')
def menuitems(request):
    items={
        'Noodles':'Price is Rs.80',
        'Burger':'Price is 70',
        'Pizza':'Price is 320',
        'Samosa':'Price is 20'
    }
    data="<h1> The items are </h1>"
    for x,y in items.items():
        data+=f"<ul> {x} - {y} </ul>"
    return HttpResponse(data)

def menuitems1(request,item):
    items={
        'Noodles':'Price is Rs.80',
        'Burger':'Price is 70',
        'Pizza':'Price is 320',
        'Samosa':'Price is 20'
    }
    data=""
    if item in items:
        data=items[item]
    else:
       data="No Item Like {item} is present."
        
    return HttpResponse(data)

def addtion(request, num1,num2):
    result=int(num1)+int(num2)
    return HttpResponse(result)

def queryAddition(request):
    num1=request.GET.get('num1')
    num2=request.GET.get('num2')
    if(num1.isdigit() and num2.isdigit()):
        result=int(num1)+int(num2)
        return HttpResponse(result)
    else:
        return HttpResponse("Invalid input")
    
def operation(request):
    value1=request.GET.get('value1')
    value2=request.GET.get('value2')
    op=request.GET.get('operation')
    if(validateOp(op)==False):
        return HttpResponse("Invalid Operation")
    elif(value1.isdigit() and value2.isdigit()):
        result=0
        if(op=="add"):
            result=int(value1)+int(value2)
        return HttpResponse(result)
    else:
        return HttpResponse(f'Invalid inputs')
    
    
def validateOp(op):
    print(op)
    if(op=="add" or op=='sub'):
        return True
    else:
        return False
    
def usernameFun(request,username):
    
    return HttpResponse(f"The username is {username}")

def userId(request,userid):
    
    return HttpResponse(f"The UserId is {userid}")

def moreParam(request,studentname,studentid):
    
    return HttpResponse(f"The Student Name is {studentname} and his id is {studentid}")

def monthYear(reqeust,month,year):
    
    return HttpResponse(f"Month is {month} and year is {year}")