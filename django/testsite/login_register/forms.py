from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password',
            }))


user = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'email',
            }))
    password_1 = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'text-control',
                'placeholder': 'password',
            }))
    password_2 = forms.CharField(
        label='Conform password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'text-control',
                'placeholder': 'Conform',
            }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = user.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('this email already exists')
        else:
            return email

    def clean_username(slef):
        username = slef.cleaned_data.get('username')
        qs = user.objects.filter(username=username)
        # print('qs is ', qs)
        if qs.exists():
            raise forms.ValidationError('this user already exists')
        else:
            return username

    def clean(self):
        data = self.cleaned_data
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')
        if password_1 != password_2:
            raise forms.ValidationError('passwords not same!')
        else:
            return data
