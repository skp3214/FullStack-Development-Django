from django.http import HttpResponse
from django.middleware.csrf import get_token


def form(request):
    csrf_token=get_token(request)
    if request.method=='GET':
        html_form=f'''
        <form  method="POST">
        <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br>
        <label for="email">Email:</label><br>
        <input type="text" id="email" name="email"><br>
        <input type="submit" value="Submit">
        '''
        return HttpResponse(html_form)
    elif request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        return HttpResponse(f'Name: {name} Email: {email}')
    
def formAdd(request):
    csrf_token=get_token(request)
    if request.method=='GET':
        html_form=f'''
        <form  method="POST">
        <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
        <label for="num1">Num1:</label><br>
        <input type="text" id="num1" name="num1"><br>
        <label for="num2">Num2:</label><br>
        <input type="text" id="num2" name="num2"><br>
        <input type="submit" value="Submit">
        '''
        return HttpResponse(html_form)
    elif request.method=='POST':
        num1=request.POST['num1']
        num2=request.POST['num2'] 
        if num1.isdigit() and num2.isdigit():
            result=int(num1)+int(num2)
            return HttpResponse(f'Result: {result}')
        else:
            return HttpResponse('Please enter valid numbers')

