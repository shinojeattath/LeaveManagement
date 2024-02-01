from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.utils import timezone
from staff.models import Staff_Details, Leave_Application, Status_Leave_Application
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings



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
                return redirect('leave_request')
            else:
                messages.error(request, "Invalid username or Password")
                return render(request, 'hod/login.html')
        else:
            messages.error(request, "Invalid username or Password")
    return render(request, 'hod/login.html')

def leave_request(request):

# app password - sljv zfrc frjx waqb
    leave_applications = Leave_Application.objects.filter()
    
    return render(request, 'hod/leave_request.html', {'leave_applications': leave_applications})

def leave_approval(request):
   # leave_applications = Leave_Application.objects.filter(name = 'TEST10')
    #########################
    if request.method == 'POST':
        # Retrieve the data from the AJAX request
        employee_id = request.POST.get('employee_id')
        no_of_days = int(request.POST.get('no_of_days'))
        department = request.POST.get('department')
        typeOfLeave = request.POST.get('leaveType')
        name = request.POST.get('name')
        leaveFrom = request.POST.get('leaveFrom')

        request.session['name'] = name
        request.session['employee_id'] = employee_id
        request.session['no_of_days'] = no_of_days
        request.session['leaveFrom'] = leaveFrom
        request.session['department'] = department

        leave_application = get_object_or_404(Staff_Details, employee_id = employee_id)
        approved_leaves = get_object_or_404(Leave_Application, employee_id = employee_id)

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

        status_of_request = 'APPROVED'

        send_mail_staff(request)
        send_mail_hr(request)


        Status_Leave_Application.objects.create(
            employee_id = approved_leaves.employee_id,
            name=approved_leaves.name,
            department=approved_leaves.department,
            nature_of_leave=approved_leaves.nature_of_leave,
            no_of_days=approved_leaves.no_of_days,
            leave_from=approved_leaves.leave_from,
            reason=approved_leaves.reason,
            alt_class_sem=approved_leaves.alt_class_sem,
            alt_hour=approved_leaves.alt_hour,
            alt_subject=approved_leaves.alt_subject,
            alt_assigned_teacher=approved_leaves.alt_assigned_teacher,
            alt_linways_assigned=approved_leaves.alt_linways_assigned,
            status_of_request = status_of_request,
            time_of_request = approved_leaves.time_of_request
        )
        approved_leaves.delete()


        return redirect('leave_request')

def  reject_leave(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')

        approved_leaves = get_object_or_404(Leave_Application, employee_id = employee_id)
        status_of_request = 'REJECTED'
        Status_Leave_Application.objects.create(
            employee_id = approved_leaves.employee_id,
            name=approved_leaves.name,
            department=approved_leaves.department,
            nature_of_leave=approved_leaves.nature_of_leave,
            no_of_days=approved_leaves.no_of_days,
            leave_from=approved_leaves.leave_from,
            reason=approved_leaves.reason,
            alt_class_sem=approved_leaves.alt_class_sem,
            alt_hour=approved_leaves.alt_hour,
            alt_subject=approved_leaves.alt_subject,
            alt_assigned_teacher=approved_leaves.alt_assigned_teacher,
            alt_linways_assigned=approved_leaves.alt_linways_assigned,
            status_of_request = status_of_request,
            time_of_request = approved_leaves.time_of_request
        )
        approved_leaves.delete()
        return redirect('leave_request')

def send_mail_staff(request):

    name = request.session.get('name', None)
    employee_id = request.session.get('employee_id', None)
    print("###")
    print(name)
    print(employee_id)

    subject = 'Leave Status'
    message = f'Entha Mwonoose Jaada aahno'
    recipient = 'diyaelfadhilph@gmail.com'
    from_mail = 'minimol.project@gmail.com'
    send_mail(subject, message, from_mail, [recipient])

def send_mail_hr(request):

    name = request.session.get('name', None)
    employee_id = request.session.get('employee_id', None)
    print("###")
    print(name)
    print(employee_id)

    subject = 'Leave Status'
    message = f'Entha Mwonoose Jaada aahno'
    recipient = 'diyaelfadhilph@gmail.com'
    from_mail = 'minimol.project@gmail.com'
    send_mail(subject, message, from_mail, [recipient])