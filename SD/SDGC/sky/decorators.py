from django.shortcuts import redirect

"""
Created a custom decorator "logout_required" as I wanted the user to be able to access:
- register.html
- login.html
- adminLog.html
ONLY if they are not logged in
"""
def logout_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('sky_home')
        return view_func(request, *args, **kwargs)
    return wrapper