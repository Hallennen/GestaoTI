from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import AcontUser
from accounts import forms
from django.views.generic import CreateView
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/aplication')
        else:
            messages.info(request, 'Usuário ou Senha inválido')
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
        
    return render(request, 'login.html', {'login_form': login_form})


class CreateUserView(CreateView):
    model = AcontUser
    form_class = forms.CreateUser
    success_url = '/login/'
    template_name = 'create.html'
