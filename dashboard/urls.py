from django.urls import path
from .views import getandcreatelisting

urlpatterns = [
    path('', getandcreatelisting, name='createlisting'),
]
