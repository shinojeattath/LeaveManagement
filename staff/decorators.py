from django.shortcuts import redirect
from django.http import HttpResponse

def hod_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.groups.filter(name='STAFF').exists():
            # Staff user detected, redirect them away
            return HttpResponse("No Access")  # Redirect to a page indicating no access
        else:
            # Non-staff user or not logged in, proceed with the view
            return view_func(request, *args, **kwargs)
    return wrapped_view

def staff_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.groups.filter(name='HOD').exists():
            # Staff user detected, redirect them away
            return HttpResponse("No Access")  # Redirect to a page indicating no access
        else:
            # Non-staff user or not logged in, proceed with the view
            return view_func(request, *args, **kwargs)
    return wrapped_view

def hr_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.groups.filter(name='HR').exists():
            # Staff user detected, redirect them away
            return HttpResponse("No Access")  # Redirect to a page indicating no access
 # Redirect to a page indicating no access
        else:
            # Non-staff user or not logged in, proceed with the view
            return view_func(request, *args, **kwargs)
    return wrapped_view
