from django.shortcuts import render


# Create your views here.
def hod_login(request):
    return render(request, 'hod/login.html')

