from django.http import HttpResponse, HttpResponseNotFound

def handler404(request,exception):
    return HttpResponseNotFound("<h1> The page you are looking for does not exist </h1>")