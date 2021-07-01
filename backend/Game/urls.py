
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('main_app.urls'), name="registerApi"),
# djngoFrontend path
    path('',include('main_app.urls')),  
]
