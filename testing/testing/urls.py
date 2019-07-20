from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('jhargram/', admin.site.urls),
    path('home/', include('creative.urls'))
]
