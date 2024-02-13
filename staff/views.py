from django.shortcuts import render, redirect, get_object_or_404
#from .models import Details, Leave_Application, Approved_Leave_Application
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.utils import timezone
from .models import Staff_Details, Leave_Application, Status_Leave_Application, AlternateArrangements
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .decorators import staff_required


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
#@staff_required
def profile(request):
    emp_id = request.session.get('username', "NONE")
    details = Staff_Details.objects.filter(employee_id = emp_id)
    if details.exists():
        detail = details[0]
    else:
        detail = None
        print(detail.emp_id)
    leave = Leave_Application.objects.filter(employee_id = emp_id)
    if leave.exists():
        leave2 = leave[0]
        if leave2.submitted == False:
            leave2.delete()

    else:
        leave2 = None

    return render(request, 'staff/profile.html', {'detail': detail})

@login_required
def signout(request):
    logout(request)
    return redirect('homepage')

@login_required
def new_leave_application(request):
    username = request.session.get('username', "NONE")

    details = Staff_Details.objects.filter(employee_id=username)
    if details.exists():
        detail = details[0] 
    else:
    # Handle the case where no matching records are found
        detail = None
    print(detail)
    if request.method == "POST":
        staff_name = request.POST['staff_name']
        department = request.POST['department']
        nature_of_leave = request.POST['leave_type']
        leave_days = request.POST['leaveDays']
        leave_period = request.POST['leave_from']
        reason_for_leave = request.POST['reason']
        linways_assigned = request.POST['leave_approval']
        time_of_request = timezone.now()
        print(reason_for_leave)
        #class_semester = request.POST['classSemester']
        #hour = request.POST['hour']
        #subject = request.POST['subject']
        #assigned_teacher = request.POST['assignedTeacher']
        
        emp_id = Staff_Details.objects.get(employee_id = username)
        leave_application = Leave_Application(
            employee_id = emp_id,
            name=staff_name,
            department=department,
            nature_of_leave=nature_of_leave,
            no_of_days=leave_days,
            leave_from=leave_period,
            reason=reason_for_leave,
            time_of_request = time_of_request,
            alt_linways_assigned=linways_assigned
            #alt_class_sem=class_semester,
            #alt_hour=hour,
            #alt_subject=subject,
            #alt_assigned_teacher=assigned_teacher,
            
            
        )
        leave_application.save()
        return redirect('new_leave_application_2')
    return render(request, 'staff/new_leave_application.html',{'detail': detail})

@login_required
@transaction.atomic
def show_leave_application(request):
    employee_id = request.session.get('username', "NONE")
    print(employee_id)

    status_of_approved_applications = Status_Leave_Application.objects.filter(employee_id = employee_id).order_by('-leave_from')
    pending_applications = Leave_Application.objects.filter(employee_id = employee_id)
    for i in status_of_approved_applications:
        print(i.status_of_request)
    
    return render(request, 'staff/show_leave_applications.html', {'status_of_approved_application': status_of_approved_applications, 'pending_applications': pending_applications})    

@transaction.atomic
def new_leave_application_2(request):
    print("leave apllication 2")
    username = request.session.get('username', "NONE")
    print(username)
    details = Staff_Details.objects.filter(employee_id=username)
    if details.exists():
        detail = details[0] 
    else:
        # Handle the case where no matching records are found
        detail = None
        print(detail)

    if request.method == 'POST':
        for i in range(1, 8):
            alt_hour_key = f'alt_hour{i}'
            alt_class_key = f'alt_class{i}'
            alt_semester_key = f'alt_semester{i}'
            alt_assigned_teacher_key = f'alt_assigned_teacher{i}'
            # Check if all keys for the current row exist in request.POST
            if alt_hour_key in request.POST and alt_class_key in request.POST \
                    and alt_semester_key in request.POST and alt_assigned_teacher_key in request.POST:
                hour1 = request.POST[alt_hour_key]
                alt_class1 = request.POST[alt_class_key]
                semester1 = request.POST[alt_semester_key]
                teacher1 = request.POST[alt_assigned_teacher_key]
                employee_id = detail
                arrangements = AlternateArrangements(
                    employee_id=employee_id,
                    alt_class=alt_class1,
                    alt_semester=semester1,
                    alt_hour=hour1,
                    alt_assigned_teacher=teacher1,
                )
                arrangements.save()
                leave = Leave_Application.objects.filter(employee_id=employee_id).order_by('id')
                first_leave = leave.first()
                first_leave.submitted = True
                first_leave.save()
            else:
                # Handle missing keys
                print(f"Keys for row {i} are missing")
        messages.success(request, "Your Application submitted successfully")
        return redirect('profile')




          # Redirect to the desired page after saving
        
    return render(request, 'staff/new_leave_application_2.html',{'detail': detail})



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

