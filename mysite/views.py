from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
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
            messages.warning(request, "Invalid password!")
            return redirect('/signup')
        
        #if username is already taken 
        try:
            if User.objects.get(username=uname):
                messages.info(request, "Username is already taken!")
                return redirect('/signup')
            
        except:
            pass

        #if email is already taken
        try:
            if User.objects.get(email=email):
                messages.info(request, "Email is already taken!")
                return redirect('/signup')
            
        except:
            pass


        myuser = User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request, "Signup successful please login!")
        return redirect('/login')
    return render(request, 'Sign-Up.html')

def login(request):
    return render(request, 'Login.html')