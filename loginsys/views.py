


from django.conf import settings
from django.contrib import auth
from media import message


from django.contrib.auth.hashers import make_password
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.contrib import messages
# Create your views here.
from django.template.context_processors import csrf

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect


from django.core.mail import send_mail


from loginsys.forms import UserForm, LoginForm



def login(request):
    args={}
    args.update(csrf(request))
    login_form = LoginForm()
    args['login_form'] = login_form
    if request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email,password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                args['login_error'] = "User is not found"
                return render(request, 'loginsys/login.html', args)
        else:
            args['login_form'] = login_form
            args['login_error'] = "login error"
            return render(request, 'loginsys/login.html', args)

    return render(request, 'loginsys/login.html', args)

def logout(request):
    return_path = request.META.get('HTTP_REFERER', '/')
    auth.logout(request)
    return redirect(return_path)




def register(request):
    args = {}
    args.update(csrf(request))
    user_form = UserForm()

    args['user_form'] = user_form


    if request.POST:
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            u = user_form.save()
            u.is_active = True
            u.save()
            email = request.POST['email']
            user = auth.authenticate(email=email, password=request.POST['password'])

            if user is not None:
                auth.login(request, user)
                subject = message.subject
                contact_message = message.contact_message % request.POST['username']
                from_email = settings.EMAIL_HOST_USER
                to_email = [email]
                send_mail(subject, contact_message, from_email, to_email)

                return redirect('/')
            else:
                raise PermissionDenied
        else:
            args['user_form'] = user_form
            args['login_error'] = "Register error"
            return render(request, 'loginsys/register.html', args)
    return render(request, 'loginsys/register.html', args)
