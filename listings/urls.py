from django.urls import path
from .views import all_listings

urlpatterns = [
    path('', all_listings, name='listings'),
]
