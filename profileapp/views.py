from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from credit.models import CreditPackage
from userapp.models import UserInfo

from .forms import ProfileEditForm
from .models import Profile

# views for dashboard


@login_required
def dashboard(request):

    userInfo = UserInfo.objects.get(user=request.user)
    properties = request.user.property_set.all()

    propertyCount = len(properties)

    return render(
        request,
        "dashboard.html",
        {"userInfo": userInfo, "propertyCount": propertyCount},
    )


@login_required
def view_profile(request):
    try:

        # get propertyCount
        properties = request.user.property_set.all()
        propertyCount = len(properties)

        # Get the profile for the authenticated user
        profile = get_object_or_404(Profile, user=request.user)
        return render(
            request,
            "profile.html",
            {"profile": profile, "propertyCount": propertyCount},
        )
    except Profile.DoesNotExist:
        # If the profile does not exist, handle it gracefully (e.g., display an error message)
        return render(request, "base.html")


@login_required
def edit_profile(request):
    try:
        # Get the profile for the authenticated user
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("view-profile")  # Redirect to the profile view
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, "edit_profile.html", {"form": form})


@login_required
def my_properties(request):

    properties = request.user.property_set.all()
    count = len(properties)

    credit = UserInfo.objects.get(user=request.user).credit

    return render(
        request,
        "my_properties.html",
        {"properties": properties, "propertyCount": count, "credit": credit},
    )


@login_required
def credits(request):

    packages = CreditPackage.objects.all()
    properties = request.user.property_set.all()
    propertyCount = len(properties)

    print("property count = ", propertyCount)

    return render(
        request,
        "buy_credits.html",
        {"packages": packages, "propertyCount": propertyCount},
    )
