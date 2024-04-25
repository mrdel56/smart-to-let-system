from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render
from django.views import View
from .import forms
from .models import Category, Location, Property
from .forms import PropertyForm
from django.db.models import Q

def home(request):
    return render(request, "home.html")


def property_list(request):
    properties = Property.objects.all()
    return render(request, "properties.html", {"properties": properties})


# class CategoryView(View):
#     def get(self, request, val):
#         property = Property.objects.filter(category=val)
#         return render(request, "category.html", locals())


# category view


def category(request, val):

    properties = Property.objects.filter(category__category_name=val, visibility=True)

    if not properties:
        messages.error(request, "No properties found in this category!")
        # return redirect("property_list")
        return render(request, "properties.html", {"properties": properties})

    return render(request, "properties.html", {"properties": properties})


# property details
def property_details(request, id):
    property = Property.objects.get(id=id)
    return render(request, "property_details.html", {"property": property})


#Contact to Owner
def contact_owner(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        return render(request, "contact_owner.html")
    else:
        return render(request, "Login.html")

# Location Views


# def location_list(request):
#     locations = Location.objects.all()
#     return render(request, "location_list.html", {"locations": locations})


# def add_location(request):
#     if request.method == "POST":
#         road_no = request.POST.get("road_no")
#         post_code = request.POST.get("post_code")
#         district = request.POST.get("district")
#         division = request.POST.get("division")
#         country = request.POST.get("country")

#         Location.objects.create(
#             road_no=road_no,
#             post_code=post_code,
#             district=district,
#             division=division,
#             country=country,
#         )
#         messages.success(request, "Location added successfully!")
#         return redirect("location_list")

#     return render(request, "add_location.html")


# def edit_location(request, location_id):
#     location = Location.objects.get(id=location_id)

#     if request.method == "POST":
#         location.area = request.POST.get("area")
#         location.road_no = request.POST.get("road_no")
#         location.upazila = request.POST.get("upazila")
#         location.post_code = request.POST.get("post_code")
#         location.district = request.POST.get("district")
#         location.save()

#         messages.success(request, "Location updated successfully!")
#         return redirect("location_list")

#     return render(request, "edit_location.html", {"location": location})


# def delete_location(request, location_id):
#     location = Location.objects.get(id=location_id)
#     location.delete()
#     messages.success(request, "Location deleted successfully!")
#     return redirect("location_list")


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful property creation
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})
