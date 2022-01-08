from django.forms import forms
from django.contrib import admin
from .models import User,Customer,Product,Cart,OrderPlaced

from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs ={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs ={'class':'form-control'}))
    email = forms.CharField(required=True,  widget=forms.EmailInput(attrs ={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('Password'),strip=False, widget=forms.TextInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))


class MypasswordchangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('old Password'), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocs':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=_('new password'), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocs':True,'class':'form-control'}),
    help_text= password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('confirm Password'), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocs':True,' class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email',max_length=200,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    newpassword1 = forms.CharField(label=_('New Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())
    newpassword2 = forms.CharField(label=_('Confirm New Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'})),