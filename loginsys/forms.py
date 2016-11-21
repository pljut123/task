from django.forms.extras import SelectDateWidget
from django.http import JsonResponse
from django.views.generic.edit import CreateView

from .models import MyUser
from django import forms
from django.utils.translation import ugettext as _



class UserForm(forms.ModelForm):
    password = forms.CharField(label=_('Password'), required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    username = forms.CharField(label=_('User Name'), required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label=_('Email'), required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    avatar = forms.ImageField(label=_('Avatar'), required=False, error_messages = {'invalid':_("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password', 'avatar']


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user




class LoginForm(forms.Form):
    email = forms.EmailField(label=_('Email'), required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(label=_('Password'), required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
