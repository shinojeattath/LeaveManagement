from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hod_login(request):
    return render(request, 'hod/login.html')

def test(request):
    return HttpResponse("hello")