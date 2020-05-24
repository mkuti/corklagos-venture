from django.shortcuts import render


# Create your views here.
def expertise(request):
    return render(request, 'expertise.html')
