from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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

    # search , sort by price, sort by price, sort by beedroom, sort by bathroom, sort by kitchen, sort by balcony, sort by floor , sorting order by asc or desc

    search = request.GET.get("search")
    sort_by = request.GET.get("sort_by")
    order = request.GET.get("order")

    # Filtering based on search query
    if search:
        properties = properties.filter(
            Q(title__icontains=search)
            | Q(description__icontains=search)
            | Q(price__icontains=search)
            | Q(category__category_name__icontains=search)
            | Q(location__area__icontains=search)
            | Q(location__upazila__icontains=search)
            | Q(location__district__icontains=search)
            | Q(location__post_code__icontains=search)
            | Q(location__road_no__icontains=search)
        )

    # Sorting based on sort_by and order parameters
    if sort_by:
        if order == "desc":
            sort_field = "-" + sort_by
        else:
            sort_field = sort_by
        properties = properties.order_by(sort_field)

    return render(
        request,
        "properties.html",
        {"properties": properties, "propertyCount": len(properties)},
    )


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
    location = Location.objects.get(id=property.location.id)

    print("property details = ", property)
    print("location details = ", location)

    return render(
        request, "property_details.html", {"property": property, "location": location}
    )


# Contact to Owner
@login_required
def contact_owner(request, id):

    propertyId = id

    # Check if the user is authenticated
    if request.user.is_authenticated:

        # Get the property
        property = Property.objects.get(id=id)

        # Get the owner of the property
        owner = property.owner

        print("Owner = ", owner)

        # get the user info of the owner
        ownerInfo = UserInfo.objects.get(user=owner.id)

        print("Owner Info = ", ownerInfo)

        return render(
            request,
            "contact_owner.html",
            {"property": property, "owner": owner, "ownerInfo": ownerInfo},
        )
    else:
        return render(request, "Login.html")


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
                owner=request.user,
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
    properties = request.user.property_set.all()
    propertyCount = len(properties)

    user_info = UserInfo.objects.get(user=request.user)

    return render(
        request,
        "add_property.html",
        {
            "categories": categories,
            "propertyCount": propertyCount,
            "user_info": user_info,
        },
    )


def delete_property(request, id):
    property = Property.objects.get(id=id)
    property.delete()
    messages.success(request, "Property deleted successfully!")
    return redirect("/dashboard/my-properties")
