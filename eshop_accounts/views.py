from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth
from .models import UserProfile
from django.contrib import messages
# Create your views here.
from eshop_accounts.forms import LoginForm, RegisterForm, UserEditForm, ProfileEditForm


# =================================== Login Page ===================================
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('username', 'A user with the entered profile could not be found.')
    context = {
        'login_form': login_form
    }
    return render(request, 'accounts/login.html', context)


# =================================== Register Page ===================================
def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        user = User.objects.create(
            username=username, email=email, first_name=first_name, last_name=last_name,
        )
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user)
        return redirect('/login')
    context = {
        'register_form': register_form,
    }
    return render(request, 'accounts/register.html', context)


# =================================== Logout ===================================
def logout_page(request):
    logout(request)
    return redirect('/login')


# =================================== Logout ===================================
@login_required
def user_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.userprofile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Successfully Updated')
            print(user_form)
            print(profile_form)
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.userprofile)
    return render(request, 'accounts/user_profile.html', {'user_form': user_form,
                                                          'profile_form': profile_form})
