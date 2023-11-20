from django.shortcuts import render

# Create your views here.
def homepage(request):
    pass

def user_login(request):
    return render(request, 'staff/login.html')