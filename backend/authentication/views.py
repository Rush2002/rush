from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def home(request):
    return render(request,"authentication/index.html")

def signup(request):

    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['Email_id']
        pass1 = request.POST['pass1']
        confirm_pass1 = request.POST['confirm_pass1']

        myuser = User.objects.create_user(username=username,password=pass1,last_name = lname, first_name = fname, email=email)

        myuser.save()
        return redirect('signin')

    return render(request,"authentication/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request, "authentication/index.html",{'fname':fname})
        else:
            messages.error(request, "Bad Credential")
            return redirect('home')

    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out succesfully!")
    return redirect("home")


