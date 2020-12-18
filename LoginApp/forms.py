from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class CreateAccountForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    verifyPassword = forms.CharField(widget=forms.PasswordInput())


class EditUserForm(forms.Form):
    pass
