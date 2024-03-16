from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def another(request):
    return render(request, 'another-page.html')

def signup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirm_password")
        #print(uname,fname,lname,email,password,confirmpassword)
        
        #if password do not match with the confirm password
        if password != confirmpassword:
            return HttpResponse("Incorrect Password!")
        
        #if username is already taken 
        try:
            if User.objects.get(username=uname):
                return HttpResponse("Username already taken")
            
        except:
            pass

        #if email is already taken
        try:
            if User.objects.get(email=email):
                return HttpResponse("Email already taken")
            
        except:
            pass


        myuser = User.objects.create_user(uname,email,password)
        myuser.save()
        return HttpResponse("Signup Successful")
    return render(request, 'Sign-Up.html')

def login(request):
    return render(request, 'Login.html')