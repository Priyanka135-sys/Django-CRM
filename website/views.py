from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):

    #checking to see if the user is logging in
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        #Authenticate

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in ")
            return redirect('home')
        else:
            messages.success(request,"There was an error while logging in! Please try again!")
            return redirect('home')
    else:
        return render (request, 'home.html' ,{})

    

def logout_users(request):
    logout(request)
    messages.success(request,"You have logged out..")
    return redirect('home')



def register_users(request):
    return render(request,'register.html' ,{})
    

# Create your views here.