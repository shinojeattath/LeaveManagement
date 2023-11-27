from django.shortcuts import render, redirect
#from .models import Details, Leave_Application, Approved_Leave_Application
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.utils import timezone
from .models import Staff_Details

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
                messages.error(request, "Invalid Employee ID or Password")
                return render(request, 'staff/login.html')
    
           
        else:
            messages.error(request, "Invalid Employee ID or Password")
            return render(request, 'staff/login.html')
    return render(request, 'staff/login.html')

@login_required
def profile(request):
    emp_id = request.session.get('username', "NONE")
    details = Staff_Details.objects.filter(employee_id=emp_id)
    if details.exists():
        detail = details[0]
    else:
        detail = None
    print(detail.name)

    return render(request, 'staff/profile.html', {'detail': detail})


@login_required
def signout(request):
    logout(request)
    return redirect('user_login')

@login_required
def leave_application(request):
    pass

@login_required
def show_leave_application(request):
    pass
def signup(request):
    if request.method == "POST":
        employeeId = request.POST['employeeId']
        ename = request.POST['ename']
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

        return redirect('user_login')  
    return render(request, 'staff/signup.html')