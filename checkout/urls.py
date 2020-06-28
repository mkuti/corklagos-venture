from django.urls import path
from .views import checkout_details

urlpatterns = [
    path('', checkout_details, name='checkout_details'),
]
