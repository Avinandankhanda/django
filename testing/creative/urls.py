from django.urls import path 
from django.views.generic import TemplateView
from . import views
urlpatterns= [
    path("",views.index,name="home"),                      # route
    path("menu/",views.menu,name="menu"),
    path("khan/",TemplateView.as_view(template_name="khan.html"),name="hotel"),
    path("new/",views.practice,name="practice"),
    path("recall/",views.recall,name="rrrrr")
]