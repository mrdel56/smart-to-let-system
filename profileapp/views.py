from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from credit.models import CreditPackage
from userapp.models import UserInfo

from .forms import ProfileEditForm
from .models import Profile

# views for dashboard


@login_required
def dashboard(request):

    user_info = UserInfo.objects.get(user=request.user)
    properties = request.user.property_set.all()

    propertyCount = len(properties)

    return render(
        request,
        "dashboard.html",
        {"user_info": user_info, "propertyCount": propertyCount},
    )


@login_required
def view_profile(request):
    try:

        # get propertyCount
        properties = request.user.property_set.all()
        propertyCount = len(properties)

        # Get the profile for the authenticated user
        # profile = get_object_or_404(Profile, user=request.user)

        user_info = UserInfo.objects.get(user=request.user)

        return render(
            request,
            "profile.html",
            {"user_info": user_info, "propertyCount": propertyCount},
        )
    except Profile.DoesNotExist:
        # If the profile does not exist, handle it gracefully (e.g., display an error message)
        return render(request, "base.html")


@login_required
def edit_profile(request):

    if request.method == "POST":
        user_info = UserInfo.objects.get(user=request.user)

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        image = request.FILES.get("image")

        try:
            user_info.first_name = first_name
            user_info.last_name = last_name
            user_info.phone = phone
            user_info.address = address
            user_info.image = image

            user_info.save()

            messages.success(request, "Profile updated successfully")

            return redirect("view-profile")
            # return redirect("edit-profile")
        except Exception as e:
            messages.error(request, "Profile update failed")
            return redirect("edit-profile")

    # for showing dashboard sidebar
    properties = request.user.property_set.all()
    propertyCount = len(properties)

    user_info = UserInfo.objects.get(user=request.user)

    return render(
        request,
        "edit_profile.html",
        {
            "propertyCount": propertyCount,
            "user_info": user_info,
        },
    )


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
