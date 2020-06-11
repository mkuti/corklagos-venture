from django.urls import path
from .views import get_and_create_listing, add_profile_details

urlpatterns = [
    path('', add_profile_details, name='editprofile'),
    path('addlisting/', get_and_create_listing, name='addlisting'),
]
