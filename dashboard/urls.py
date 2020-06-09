from django.urls import path
from .views import create_or_edit_listing

urlpatterns = [
    path('', create_or_edit_listing, name='create_or_edit_listing'),
]
