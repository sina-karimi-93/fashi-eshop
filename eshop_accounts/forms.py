from django import forms
from django.contrib.auth.models import User
from django.core import validators
# from django.core.files.images import get_image_dimensions
from .models import UserProfile


# =================================== Avatar ======================================
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('date_of_birth','phone', 'image')
        widgets = {
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


# =================================== Login Form ===================================
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please enter your username'}),
        label='Username'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Please enter your password'}),
        label='Password'
    )

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     is_exist_username = User.objects.filter(username=username)
    #     if not is_exist_username:
    #         raise forms.ValidationError('A user with the entered profile has not registered.')
    #     return username


# =================================== Register Form ===================================
class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
        label='First Name'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
        label='Last Name'
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please enter your username'}),
        label='Username',
        validators=[
            validators.MaxLengthValidator(limit_value=20,
                                          message='The number of characters entered cannot be more than 20.'),
            validators.MinLengthValidator(limit_value=3,
                                          message='The number of characters entered can not be less than 3.')
        ]
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Please enter an valid email'}),
        label='Email',
        validators=[
            validators.EmailValidator('The entered email is invalid.')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Please enter your password'}),
        label='Password',
        validators=[
            validators.MinLengthValidator(limit_value=10, message='Please add at least 10 character')
        ]
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Please re-enter your password again'}),
        label='Re-enter Password'
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exist_user_by_username = User.objects.filter(username=username)
        if is_exist_user_by_username:
            raise forms.ValidationError('This user has already registered')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exist_user_by_email = User.objects.filter(email=email)
        if is_exist_user_by_email:
            raise forms.ValidationError('The entered email has already been used.')

        if len(email) > 25:
            raise forms.ValidationError('Email characters must be less than 25')

        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('Passwords does not match.')
