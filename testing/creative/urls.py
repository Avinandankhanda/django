from django.urls import path 
from django.views.generic import TemplateView
from . import views
urlpatterns= [
    path("",views.home,name="home"),                      # route
    path("menu/",views.menu,name="menu"),
    path("hotel/",TemplateView.as_view(template_name="hotel.html"),name="hotel")
]