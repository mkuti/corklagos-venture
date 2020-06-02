from django.urls import path
from .views import expertise

urlpatterns = [
    path('expertise/', expertise, name='expertise'),
]
