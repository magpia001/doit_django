from django.urls import path
from .views import landing, about_me 

urlpatterns = [
    path('', landing, name='landing'),
    path('about_me/', about_me, name='about_me'),
]