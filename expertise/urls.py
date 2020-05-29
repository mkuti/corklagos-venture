from django.urls import path
from .views import expertise

urlpatterns = [
    path('', expertise, name='expertise'),
]
