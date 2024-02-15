from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'hr/hrhome.html',{'applications': applications})

def staff_profile_hr(request):
    employee_id = request.session.get('staff_employee_id_hr')
    print(employee_id)
    details = Staff_Details.objects.filter(employee_id = employee_id)
    if details.exists():
        detail = details[0]
    else:
        detail = None
    return render(request, 'hr/staff_profile.html', {'detail': detail})

def data_from_ajax_hr(request):
    if request.method == 'POST':
        # Extract the employee ID from the POST data
        employee_id = request.POST.get('employee_id')
        request.session['staff_employee_id_hr'] = employee_id
        print("eaefsas")
        print(employee_id)
        return redirect('staff_profile_hr')
   
def cs_d(request):
    application = Staff_Details.objects.filter(department = 'CSE')
    return render(request, 'hr/hrcse.html',{'application':application})
def eee_d(request):
    application = Staff_Details.objects.filter(department = 'EEE')
    return render(request, 'hr/hreee.html',{'application':application}) 

def ece_d(request):
    application = Staff_Details.objects.filter(department = 'ECE')
    return render(request, 'hr/hrece.html',{'application':application})  

def me_d(request):
    application = Staff_Details.objects.filter(department = 'ME')
    return render(request, 'hr/hrme.html',{'application':application}) 

def ce_d(request):
    application = Staff_Details.objects.filter(department = 'CE')
    return render(request, 'hr/hrce.html',{'application':application}) 

def ash_d(request):
    application = Staff_Details.objects.filter(department = 'ASH')
    return render(request, 'hr/hrash.html',{'application':application}) 

def show_d(request):
    return render(request, 'hr/Hrdepts.html')

def show_l(request):
    return render(request, 'hr/hrleave.html')

def hr_leave_requests(request):
    applications = Status_Leave_Application.objects.filter(status_of_request = 'APPROVED')
    return render(request, 'hr/hr_leave_request.html',{'applications':applications})

def staff_profile_hr(request):
    emp_id = request.session.get('staff_employee_id', "NONE")
    details = Staff_Details.objects.filter(employee_id = emp_id)
    if details.exists():
        detail = details[0]
    else:
        detail = None
        print(detail.emp_id)
    return render(request, 'hod/staff_profile.html', {'detail': detail})

def data_from_ajax_hr(request):
    if request.method == 'POST':
        # Extract the employee ID from the POST data
        employee_id = request.POST.get('employee_id')
        request.session['staff_employee_id'] = employee_id
        print("eaefsas")
        print(employee_id)
        return redirect('view_request')