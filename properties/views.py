from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, render
from django.views import View

from userapp.models import UserInfo

from . import forms
from .forms import LocationForm, PropertyForm
from .models import Category, Location, Property


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


# Contact to Owner
@login_required
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
    if request.method == "POST":

        userInfo = UserInfo.objects.get(user=request.user)

        if userInfo.credit < 5:
            messages.error(request, "You don't have enough credit to add property!")
            return redirect("add-property")

        try:
            data = request.POST
            title = data.get("title")
            category = data.get("category")
            description = data.get("description")
            rooms = data.get("rooms")
            washrooms = data.get("washrooms")
            kitchen = data.get("kitchen")
            balcony = data.get("balcony")
            floor = data.get("floor")
            price = data.get("price")
            property_img = request.FILES.get("property_img")

            area = data.get("area")
            road_no = data.get("road_no")
            upazila = data.get("upazila")
            post_code = data.get("post_code")
            district = data.get("district")

            category = Category.objects.get(id=category)

            # validate all fields for location
            if not area or not road_no or not upazila or not post_code or not district:
                messages.error(request, "All fields are required!")
                return redirect("add-property")

            location = Location.objects.create(
                area=area,
                road_no=road_no,
                upazila=upazila,
                post_code=post_code,
                district=district,
            )

            # validate all fields

            if (
                not title
                or not category
                or not description
                or not rooms
                or not washrooms
                or not kitchen
                or not balcony
                or not floor
                or not price
                or not property_img
                or not location
            ):
                messages.error(request, "All fields are required!")
                return redirect("add-property")

            property = Property.objects.create(
                title=title,
                category=category,
                description=description,
                rooms=rooms,
                washrooms=washrooms,
                kitchen=kitchen,
                balcony=balcony,
                floor=floor,
                price=price,
                property_img=property_img,
                location=location,
            )

            userInfo.credit -= 5
            userInfo.save()

            messages.success(request, "Property added successfully!")
            return redirect("add-property")
        except:
            messages.error(request, "Error adding property!")
            return redirect("add-property")

    categories = Category.objects.all()

    return render(request, "add_property.html", {"categories": categories})


# def add_property(request):
#     if request.method == "POST":
#         form = PropertyForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Property added successfully!")
#             return redirect("property_list")
#         else:
#             messages.error(request, "Error adding property!")
#             return redirect("add-property")

#     return render(request, "add_property.html")
