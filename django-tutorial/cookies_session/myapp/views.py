from django.http import HttpResponse
from django.shortcuts import render
def setCookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('username', 'John Doe', max_age=15)  # Cookie expires in 1 hour
    return response

def getCookie(request):
    username = request.COOKIES.get('username')
    if username:
        return HttpResponse(f"Hello {username}")
    else:
        return HttpResponse("No cookie found")

def deleteCookie(request):
    response = HttpResponse("Cookie Deleted")
    response.delete_cookie('username')
    return response

def setLightDarkTheme(request):
    if request.method == 'POST':
        theme = request.POST.get('theme')
        response = render(request, 'lightdark.html', {'theme': theme})
        response.set_cookie('theme', theme, max_age=3600)
        return response
    else:
        theme = request.COOKIES.get('theme')
        if theme:
            return render(request, 'lightdark.html', {'theme': theme})
        
def page1(request):
    response = HttpResponse("Welcome to Page 1")
    response.set_cookie('last_visited_page', 'page1', max_age=3600)  # Cookie expires in 1 hour
    return response

def page2(request):
    response = HttpResponse("Welcome to Page 2")
    response.set_cookie('last_visited_page', 'page2', max_age=3600)  # Cookie expires in 1 hour
    return response

def page3(request):
    response = HttpResponse("Welcome to Page 3")
    response.set_cookie('last_visited_page', 'page3', max_age=3600)  # Cookie expires in 1 hour
    return response

def lastVisitedPage(request):
    last_visited_page = request.COOKIES.get('last_visited_page')
    return render(request, 'last_visited_page.html', {'last_visited_page': last_visited_page})
        
def pageNow(request):
    return render(request, 'page.html')