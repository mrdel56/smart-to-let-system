from django.shortcuts import render,HttpResponse,redirect
from .models import  Profile
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .forms import ProfileEditForm

from django.shortcuts import render, get_object_or_404
from .models import Profile

def view_profile(request):
    try:
        # Try to get the profile for the current user
        profile = get_object_or_404(Profile, user=request.user)
        return render(request, "profile.html", {"profile": profile})
    except Profile.DoesNotExist:
        # If the profile does not exist, handle it gracefully (e.g., display an error message)
        return render(request, "profile_not_found.html")
    
    

from .forms import ProfileEditForm

def edit_profile(request):
    # Get the current user's profile
    profile = request.user.profile

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():            
            form.save()
            return redirect('view-profile')  
    else:
        # Create a form instance and populate it with the current profile data
        form = ProfileEditForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})