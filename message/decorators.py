from django.shortcuts import redirect

def is_authenticated(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        elif not request.user.is_authenticated:
            return redirect('home')
        return wrap

