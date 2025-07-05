from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register_page(request):
 if request.method == "POST":
    username=request.POST.get('Num1')
    password=request.POST.get('Num2')
    conpassword=request.POST.get('Num3')
    if conpassword!=password:
        return render(request,'register.html',{'error':'error'})
    user=user.objects.create_user(username=username,password=password)
    return redirect('login_page')
    return render(request,'login.html')
    return render(request,'register.html')
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")
def home_page(request):
    return render(request,'home.html')
def logout_page(request):
    return redirect('login_page')    

