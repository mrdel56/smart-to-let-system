from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import Property
from .models import Location
from django.contrib import messages


def home(request):
    return render(request, "home.html")


class CategoryView(View):
    def get(self, request, val):
        property = Property.objects.filter(category=val)
        return render(request, "category.html", locals())


# Location Views


def location_list(request):
    locations = Location.objects.all()
    return render(request, "location_list.html", {"locations": locations})


def add_location(request):
    if request.method == "POST":
        road_no = request.POST.get("road_no")
        post_code = request.POST.get("post_code")
        district = request.POST.get("district")
        division = request.POST.get("division")
        country = request.POST.get("country")

        Location.objects.create(
            road_no=road_no,
            post_code=post_code,
            district=district,
            division=division,
            country=country,
        )
        messages.success(request, "Location added successfully!")
        return redirect("location_list")

    return render(request, "add_location.html")


def edit_location(request, location_id):
    location = Location.objects.get(id=location_id)

    if request.method == "POST":
        location.area = request.POST.get("area")
        location.road_no = request.POST.get("road_no")
        location.upazila = request.POST.get("upazila")
        location.post_code = request.POST.get("post_code")
        location.district = request.POST.get("district")
        location.save()

        messages.success(request, "Location updated successfully!")
        return redirect("location_list")

    return render(request, "edit_location.html", {"location": location})


def delete_location(request, location_id):
    location = Location.objects.get(id=location_id)
    location.delete()
    messages.success(request, "Location deleted successfully!")
    return redirect("location_list")
