from django.shortcuts import render, redirect
#from .models import Details, Leave_Application, Approved_Leave_Application
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.utils import timezone
from staff.models import Staff_Details, Leave_Application, Status_Leave_Application

# Create your views here.

def hod_login(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            if user.groups.filter(name='HOD').exists():
                message = messages.error(request,"invalid")
                print("12234")
                print(message)
                return redirect('leave_requests')
            else:
                messages.error(request, "Invalid username or Password")
                message = messages.error(request,"invalid")
                print(message)
                print("12234")
                return render(request, 'hod/login.html')
                print(messages)
        else:
            messages.error(request, "Invalid username or Password")
            print("12234")
            return render(request, 'hod/login.html')


    return render(request, 'hod/login.html')

def leave_requests(request):
    return HttpResponse("hofjo")

