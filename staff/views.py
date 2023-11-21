from django.shortcuts import render, redirect
#from .models import Details, Leave_Application, Approved_Leave_Application
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def homepage(request):
    pass

def user_login(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            if user.groups.filter(name='STAFF').exists():
                return redirect('profile')
            else:
                messages.error(request, "Invalid username or Password")
                return render(request, 'staff/login.html')
    
           
        else:
            messages.error(request, "Invalid username or Password")
            return render(request, 'staff/login.html')
    return render(request, 'staff/login.html')

def profile(request):
    return render(request, 'staff/profile.html')
def signout(request):
    pass
def leave_application(request):
    pass
def show_leave_application(request):
    pass
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        #password1 = request.POST['password1']

        
        user = User.objects.create_user(username,email,password)
        user.save()
        return redirect('user_login')  
    return render(request, 'staff/signup.html')