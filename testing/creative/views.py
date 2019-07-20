from django.http import HttpResponse 

def home(request):
    return HttpResponse("Welcome to the world of Avinandan Khanda")

def menu(request):
    return HttpResponse("it's my web-site")
