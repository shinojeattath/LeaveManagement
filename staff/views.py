from django.shortcuts import render, redirect
#from .models import Details, Leave_Application, Approved_Leave_Application
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.utils import timezone
from .models import Staff_Details, Leave_Application, Status_Leave_Application

# Create your views here.
def homepage(request):
    return render(request, 'staff/homepage.html')

def user_login(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            print(username)
            if user.groups.filter(name='STAFF').exists():
                return redirect('profile')
            else:
                logout(request)
                messages.error(request, "Invalid Employee ID or Password")
                return render(request, 'staff/login.html')
    
           
        else:
            messages.error(request, "Invalid Employee ID or Password")
            return render(request, 'staff/login.html')
    return render(request, 'staff/login.html')

@login_required
def profile(request):
    emp_id = request.session.get('username', "NONE")
    details = Staff_Details.objects.filter(employee_id = emp_id)
    if details.exists():
        detail = details[0]
    else:
        detail = None
        print(detail.emp_id)

    return render(request, 'staff/profile.html', {'detail': detail})

@login_required
def signout(request):
    logout(request)
    return redirect('user_login')

@login_required
def new_leave_application(request):
    username = request.session.get('username', "NONE")
    do_exist = Leave_Application.objects.filter(employee_id = username)

    if do_exist.exists():
        messages.warning(request,"You have already applied for a leave.")
        return redirect('profile')
        
    else:

        details = Staff_Details.objects.filter(employee_id=username)
        if details.exists():
            detail = details[0] 
        else:
        # Handle the case where no matching records are found
            detail = None
        print(detail.name)
        if request.method == "POST":
            staff_name = request.POST['staffName']
            department = request.POST['department']
            nature_of_leave = request.POST['natureOfLeave']
            leave_days = request.POST['leaveDays']
            leave_period = request.POST['leavePeriod']
            reason_for_leave = request.POST['reasonForLeave']
            class_semester = request.POST['classSemester']
            hour = request.POST['hour']
            subject = request.POST['subject']
            assigned_teacher = request.POST['assignedTeacher']
            linways_assigned = request.POST['linwaysAssigned']

            time_of_request = timezone.now()
            emp_id = Staff_Details.objects.get(employee_id = username)


            leave_application = Leave_Application(
                employee_id = emp_id,
                name=staff_name,
                department=department,
                nature_of_leave=nature_of_leave,
                no_of_days=leave_days,
                leave_from=leave_period,
                reason=reason_for_leave,
                alt_class_sem=class_semester,
                alt_hour=hour,
                alt_subject=subject,
                alt_assigned_teacher=assigned_teacher,
                alt_linways_assigned=linways_assigned,
                time_of_request = time_of_request
            )
            leave_application.save()
            messages.success(request, "Your Application submitted successfully")
            return redirect('profile')
    return render(request, 'staff/new_leave_application.html',{'detail': detail})

@login_required
def show_leave_application(request):
    employee_id = request.session.get('username', "NONE")
    print(employee_id)

    status_of_approved_applications = Status_Leave_Application.objects.filter(employee_id = employee_id).order_by('-leave_from')
    
    pending_applications = Leave_Application.objects.filter(employee_id = employee_id)
    
    return render(request, 'staff/show_leave_applications.html',{'status_of_approved_applications': status_of_approved_applications, 'pending_applications': pending_applications})
    
def signup(request):
    if request.method == "POST":
        employeeId = request.POST['employeeId']
        ename = request.POST['name']
        department = request.POST['department']
        designation = request.POST['designation']
        email = request.POST['email']
        password = request.POST['password']

        #password1 = request.POST['password1']


        
        user = User.objects.create_user(employeeId,email,password)
        user.save()
        Staff_Details.objects.create(
            employee_id = employeeId,
            name = ename,
            email = email,
            department = department,
            designation = designation,
            cl1_bal = 6,
            cl2_bal = 6,
            ML_bal = 10,
            VL_bal = 10,
            DL_bal = 10,
            LoP = 0,
            comp_off = 0
        )

        return redirect('signup')  
    return render(request, 'staff/signup.html')