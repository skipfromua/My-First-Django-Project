from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.contrib.auth.forms import UserCreationForm


def logout_func(request):
    logout(request)
    return redirect('main')


class LoginView(View):

    def get(self, request):
        return render(request, 'Accounts/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('main')
            else:
                context = {
                    'Error': 'User is inactive'
                }
                return render(request, 'Accounts/login.html', context)
        else:
            context = {
                'Error': 'Login/Password error'
            }
            return render(request, 'Accounts/login.html', context)


class RegistrationView(View):

    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'Accounts/registration.html', context)

    def post(self, request):
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = authenticate(username=newuser_form.cleaned_data['username'],
                                   password=newuser_form.cleaned_data['password2'])
            login(request, newuser)
            return redirect('main')
        else:
            context = {
                'form': newuser_form,
                'Error': 'Invalid data'
            }
        return render(request, 'Accounts/registration.html', context)
