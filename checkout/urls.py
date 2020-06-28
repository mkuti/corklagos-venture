from django.urls import path
from .views import checkout_details


app_name = "checkout"
urlpatterns = [
    path('', checkout_details, name='checkout_details'),
]
