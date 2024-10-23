from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('admin')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
        
    return render(request, 'login.html', {'login_form': login_form})
