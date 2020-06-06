from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
@login_required
def profile(request):
    """ Display the member's profile after login. """
    # profile = get_object_or_404(Profile, user=request.user)

    # template = 'profile.html'
    context = {
        # 'profile': profile,
    }

    return render(request, 'profile.html', context)
