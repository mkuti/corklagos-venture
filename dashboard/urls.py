from django.urls import path
from .views import createlisting

urlpatterns = [
    path('', createlisting, name='createlisting'),
]
