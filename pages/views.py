from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def expertise(request):
    return render(request, 'expertise.html')
