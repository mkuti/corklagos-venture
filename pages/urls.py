from django.urls import path
from .views import expertise

app_name = 'pages'
urlpatterns = [
    path('expertise/', expertise, name='expertise'),
]
