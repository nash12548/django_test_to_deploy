from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm


# Create your views here.

def login_page(request):
    login_forms = LoginForm(request.POST or None)
    context = {
        'forms': login_forms,
    }
    if login_forms.is_valid():
        print(login_forms.cleaned_data)
        username = login_forms.cleaned_data.get('username')
        password = login_forms.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        context['forms'] = LoginForm()
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            print('login fail')
            # return redirect('login_page')
    return render(request, 'login_register/login.html', context)


user = get_user_model()


def register_page(request):
    register_forms = RegisterForm(request.POST or None)
    context = {
        'forms': register_forms
    }
    if register_forms.is_valid():
        print(register_forms.cleaned_data)
        context['forms'] = RegisterForm()
        username = register_forms.cleaned_data.get('username')
        email = register_forms.cleaned_data.get('email')
        password = register_forms.cleaned_data.get('password_1')
        new_user = user.objects.create_user(username, email, password)
        print(new_user)
    return render(request, 'login_register/register.html', context)
