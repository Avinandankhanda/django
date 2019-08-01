from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to the world of Avinandan Khanda")

def menu(request):
    return HttpResponse("it's my web-site")

def new(request):
    return HttpResponse("no body can see it")

def practice(request): 
    html="""
   
    <h1>it is my firt sight if any disapointment please contact me</h1>
    """
    return HttpResponse(html)
def recall(request):
    html="""
    
    <h1>i am re calling the project<h1/>
    """
    return HttpResponse(html)
def index(request):
    template_name="index.html"
    context={
        "name":'Avinandan Khanda',
        "age":17
            }
    return render(request, template_name,context)