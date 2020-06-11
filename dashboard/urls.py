from django.urls import path
from .views import getandcreatelisting, addprofiledetails

urlpatterns = [
    path('', addprofiledetails, name='editprofile'),
    path('addlisting/', getandcreatelisting, name='addlisting'),
]
