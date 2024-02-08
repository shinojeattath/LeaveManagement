from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from staff.models import Staff_Details, Leave_Application, Status_Leave_Application
from django.core.serializers import serialize

# Create your views here.
def hr_login(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            if user.groups.filter(name='HR').exists():
                return redirect('hr_homepage')
            else:
                messages.error(request, "Invalid username or Password")
                return render(request, 'hod/login.html')
        else:
            messages.error(request, "Invalid username or Password")
    return render(request, 'hr/login.html')

def hr_homepage(request):
    applications = Status_Leave_Application.objects.filter(status_of_request = 'APPROVED')
    print(applications)
    return render(request, 'hr/HRdept.html',{'applications': applications})

