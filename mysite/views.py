from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_process
from django.contrib.auth import logout as logout_process
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render
from profileapp.models import Profile
from properties.models import Property

def base(request):
    return render(request, "base.html")

def home(request):
    profile = Profile.objects.get(user=request.user)
    properties = Property.objects.all()
    return render(request, "home.html", {"profile": profile, "properties": properties})


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
        # return HttpResponse("Signup Successful")
        messages.success(request, "Signup successful please login!")
        return redirect("/login")
    return render(request, "Sign-Up.html")


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
    return redirect("login")


from django.views import View


class CategoryView(View):
    def get(self, request):
        return render(request, "category.html")
