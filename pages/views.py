from django.shortcuts import render, redirect, reverse


# Create your views here.
def home(request):
    user = request.user
    if user.is_authenticated:
        return redirect(reverse('listings'))

    return render(request, 'home.html')


def expertise(request):
    return render(request, 'expertise.html')
