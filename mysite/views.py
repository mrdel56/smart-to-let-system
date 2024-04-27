from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_process
from django.contrib.auth import logout as logout_process
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import HttpResponse, redirect, render

from profileapp.models import Profile
from properties.models import Location, Property
from userapp.models import UserInfo


def base(request):
    return render(request, "base.html")


# def home(request):
#     properties = Property.objects.all()
#     locations = Location.objects.all()

#     # give latest 8 properties
#     properties = properties.order_by("-id")[:8]

#     return render(
#         request, "home.html", {"properties": properties, "locations": locations}
#     )

from django.db.models import Count

def home(request):
    properties = Property.objects.all()
    locations = Location.objects.all()
    # Get all properties ordered by the latest ones
    properties = Property.objects.order_by("-id")[:8]

    # Get all unique locations
    # locations = Location.objects.values_list("name", flat=True).distinct()[:6]
    # locations = Location.objects.annotate(property_count=Count('property')).filter(property_count__gt=1)
    # locations_with_counts = Location.objects.annotate(property_count=Count('property'))

    # Sort locations by property count in descending order and get the top 5
    # locations = locations_with_counts.order_by('-property_count')[:2] 
    # locations = Location.objects.annotate(property_count=Count('property')).order_by('-[property_count]_count')[:5]
    locations = Location.objects.values('area','district').annotate(property_count=Count('property')).order_by('-property_count')[:8] 

    return render(
        request, "home.html", {"properties": properties, "locations": locations}
    )






# profile = Profile.objects.get(user=request.user)
#
# return render(request, 'home.html', {'profile': profile, 'properties': properties})


def signup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        # print(uname,fname,lname,email,password,confirmpassword)

        # if password do not match with the confirm password
        if password != confirm_password:
            # return HttpResponse("Incorrect Password!")
            messages.error(request, "Invalid password!")
            return redirect("/signup")

        # if password is less than 8 characters
        if len(password) < 8:
            # return HttpResponse("Password is too short!")
            messages.error(request, "Password should be at least 8 characters long!")
            return redirect("/signup")

        # if username is already taken
        try:
            if User.objects.get(username=uname):
                # return HttpResponse("Username already taken")
                messages.info(request, "Username is already taken!")
                return redirect("/signup")

        except:
            pass

        # if email is already taken
        try:
            if User.objects.get(email=email):
                # return HttpResponse("Email already taken")
                messages.info(request, "Email is already taken!")
                return redirect("/signup")

        except:
            pass

        user = User.objects.create_user(
            username=uname,
            email=email,
            password=password,
            first_name=fname,
            last_name=lname,
        )
        user.save()

        # create user profile
        # user_info = UserInfo.objects.create(
        #     user=user,
        #     first_name=fname,
        #     last_name=lname,
        #     phone="",
        #     address="",
        #     image="",
        #     credit=0,
        # )

        # user_info.save()

        # return HttpResponse("Signup Successful")
        messages.success(request, "Signup successful please login!")
        return redirect("/login")
    return render(request, "Sign-Up.html")


@receiver(post_save, sender=User)
def create_user_info(sender, instance, created, **kwargs):
    """
    Signal receiver function to create UserInfo object when a User is created.
    """
    if created:
        # UserInfo.objects.create(
        #     user=instance,
        #     first_name=instance.first_name,
        #     last_name=instance.last_name,
        # )
        UserInfo.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            phone="",
            address="",
            image="",
            credit=0,
        )


@receiver(post_save, sender=User)
def save_user_info(sender, instance, **kwargs):
    """
    Signal receiver function to save UserInfo object when a User is saved.
    """
    instance.userinfo.save()


def login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        password = request.POST.get("password")
        myuser = authenticate(username=uname, password=password)
        if myuser is not None:
            login_process(request, myuser)
            messages.success(request, "Login Successfully")
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("/login")
    return render(request, "Login.html")


def logout(request):
    logout_process(request)
    messages.info(request, "Logout Successful")
    return redirect("/login")


from django.views import View


class CategoryView(View):
    def get(self, request):
        return render(request, "category.html")

def about(request):
    return render(request, "about.html")