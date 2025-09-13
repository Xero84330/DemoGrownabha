from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def dashboard(request):
    return render(request, 'student/studentdb.html')

def lectures(request):
    return render(request, 'student/lectures.html')


# this is signup function
def signup_view(request):
    if request.method == "POST":
        username= request.POST.get("username")
        email= request.POST.get("email")
        password= request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect("login")

    return render(request, "student/signup.html")
# this is login function

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.username}")
            return redirect("dashboard")   # homepage
        else:
            messages.error(request, "Invalid credentials")
            return redirect("/")

    return render(request, "student/login.html")