from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from staff.models import Staff_Details, Leave_Application, Status_Leave_Application
from django.core.serializers import serialize
from .models import Leave_Application_hr
from staff.models import *
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
def duty_l(request):
    application = Leave_Application_hr.objects.all()
    return render(request,'hr/dutyleave.html',{'application':application})
def view_dl(request):
    return render(request, 'hr/hrshowleave.html')

def view_requests_hr(request):

    leave_applications = None
    arrangements = None
    

    employee_id = request.session.get('staff_employee_id')
    print("------======------")
    print(employee_id)
    profile = get_object_or_404(Staff_Details, employee_id = employee_id)
    department = profile.department
    leave_applications = Leave_Application_hr.objects.filter(employee_id = employee_id)
    arrangements = AlternateArrangements.objects.filter(employee_id = employee_id)
        
    for a in leave_applications:
        print(a.name)
        print(a.nature_of_leave)

            
    gap_counter = 1

    return render(request, 'hr/view_request_hr.html',{'leave_applications': leave_applications, 'arrangements': arrangements, 'gap_counter':gap_counter})

def leave_approval_hr(request):
   
    
    employee_id = request.session.get('staff_employee_id')
    print('1111111111111111111111')
    print(employee_id)
    #no_of_days = int(request.POST.get('no_of_days'))
    ##department = request.POST.get('department')
   # typeOfLeave = request.POST.get('leaveType')
    #name = request.POST.get('name')
    #leaveFrom = request.POST.get('leaveFrom')
    
    leave_application = get_object_or_404(Staff_Details, employee_id = employee_id)
    approved_leaves = get_object_or_404(Leave_Application_hr, employee_id = employee_id)
    alternate = AlternateArrangements.objects.filter(employee_id = employee_id)

    typeOfLeave = approved_leaves.nature_of_leave
    no_of_days = int(approved_leaves.no_of_days)
    if typeOfLeave == "CL1":
        numberofleaves = int(leave_application.cl1_bal)
    elif typeOfLeave == "CL2":
        numberofleaves = int(leave_application.cl2_bal)
    elif typeOfLeave == "ML":
        numberofleaves = int(leave_application.ML_bal)
    elif typeOfLeave == "VL":
        numberofleaves = int(leave_application.VL_bal)
    elif typeOfLeave == "DL":
        numberofleaves = int(leave_application.DL_bal)
    elif typeOfLeave == "LoP":
        numberofleaves = int(leave_application.LoP)
    left = numberofleaves - no_of_days
    
    try:
        if typeOfLeave == "CL1":
            leave_application.cl1_bal = left
        elif typeOfLeave == "CL2":
            leave_application.cl2_bal = left
        elif typeOfLeave == "ML":
            leave_application.ML_bal = left
        elif typeOfLeave == "VL":
            leave_application.VL_bal = left
        elif typeOfLeave == "DL":
            leave_application.DL_bal = left
        elif typeOfLeave == "LoP":
            leave_application.LoP = left
        leave_application.save()

    except Exception as e:
        messages.error(request, "No Requested leaves left")
        return redirect('view_request')
    
    
    status_of_request = 'APPROVED'
    #send_mail_staff(request)
    #send_mail_hr(request)
    Status_Leave_Application.objects.create(
        employee_id = approved_leaves.employee_id,
        name=approved_leaves.name,
        department=approved_leaves.department,
        nature_of_leave=approved_leaves.nature_of_leave,
        no_of_days=approved_leaves.no_of_days,
        leave_from=approved_leaves.leave_from,
        reason=approved_leaves.reason,
        status_of_request = status_of_request,
        time_of_request = approved_leaves.time_of_request
    )
    approved_leaves.delete()
    alternate.delete()
    return redirect('duty_l')

def reject_leave_hr(request):
    
    employee_id = request.session.get('staff_employee_id')
    print(employee_id)
    #send_mail_hr(request)
    emp = get_object_or_404(Staff_Details, employee_id = employee_id)
    approved_leaves = get_object_or_404(Leave_Application_hr, employee_id = employee_id)
    status_of_request = 'REJECTED'
    Status_Leave_Application.objects.create(
        employee_id = emp,
        nature_of_leave=approved_leaves.nature_of_leave,
        no_of_days=approved_leaves.no_of_days,
        leave_from=approved_leaves.leave_from,
        status_of_request = status_of_request,
        time_of_request = approved_leaves.time_of_request
    )
    approved_leaves.delete()
    arrangements = AlternateArrangements.objects.filter(employee_id = employee_id)
    arrangements.delete()
    return redirect('leave_request_hr')