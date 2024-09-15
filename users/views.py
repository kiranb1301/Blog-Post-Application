from django.shortcuts import render
from  .models import Bloggers
from .forms import *
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth import login
from django.contrib import sessions
from django.contrib.auth import authenticate, update_session_auth_hash,logout
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect 
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings


def signup_view(request):
    if request.method == 'POST':
        form1 = Register(request.POST) 
        if form1.is_valid():
            nm = form1.cleaned_data.get('name')
            em = form1.cleaned_data.get('email')
            pm = make_password(form1.cleaned_data.get('password'))  # Hashing the password
            mo = form1.cleaned_data.get('mobile')
            gen = form1.cleaned_data.get('gender') 
            Bloggers(name=nm, email=em, password=pm, mobile=mo, gender=gen).save() 
            
        else:
            return render(request,'users/sign_up.html',{'form':form1})
    else:
        form1 = Register()
    return render(request,'users/sign_up.html',{'form':form1})



def login_view(request):
    return_url = request.GET.get('next', None)
    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        if form1.is_valid():
            email = form1.cleaned_data.get('email')
            password = form1.cleaned_data.get('password')
            print(f"Attempting to authenticate user with email: {email}")  # Debug statement
            user = authenticate(request, email=email, password=password)
            if user is not None:
                    login(request, user,backend='users.backends.BloggersBackend')  # Manually logging in
                    request.session['email'] = email
                    messages.success(request, 'You have logged in successfully!!!')
                    print('user successfuly logged in')
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:        
                        return redirect('blog-index')  
            else:
                messages.error(request, 'Invalid email or password')
                print('its error')
                return redirect('login')
            
        else:
            print("Form is not valid")
            messages.error(request, 'Please correct the error below.')
    else:
        form1 = LoginForm()
    return render(request, 'users/login.html', {'form1': form1})

#Logout View
@login_required(login_url='user-login')
def logout1(request):
    logout(request)
    request.session.clear()
    messages.success(request, 'You have been logged out successfully.')
    return redirect('blog-index') 


#View of user profile
@login_required(login_url='user-login') 
def profile_view(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})


#View for password change

@login_required 
def change_password(request):
    error = None
    if request.method =='POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save() 
            update_session_auth_hash(request,user)
            messages.success(request,'Your password was successfully Updated')
            print("your password is Updated SUccessfully")
            return redirect('user-profile')
        else:
            'Please correct the error below'
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'changepassword.html',{'form':form,'error':error})
