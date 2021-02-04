from django.urls import path
from paginas.views import home, sobre

urlpatterns = [
    path('home/', home),
    path('about/', sobre),
    
]