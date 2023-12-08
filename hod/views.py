from django.shortcuts import render



# Create your views here.
def hod_login(request):
    return render(request, 'hod/login.html')

def leave_request(request):
    return render(request, 'hod/leave_request.html')
