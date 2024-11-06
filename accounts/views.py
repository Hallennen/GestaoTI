from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import AcontUser
from aplication.models import Folga
from accounts import forms
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView,ListView
from django.contrib import messages
from django.urls import reverse_lazy

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


## logout 
def logout_view(request):
    logout(request)
    return redirect ('login')



class AplicationView(TemplateView):
    template_name = 'aplication.html'   


    def get_context_data(self, **kwargs):
        context = Folga.objects.filter(status_folga = 'APR')
        extra_context = (Folga.objects.filter(status_folga = 'APR').count())
        extra = [extra_context]
        context = context
        return ({'context':context, 'contadores':extra_context})



class DetailProfileView(DetailView):
    model = AcontUser
    template_name = 'Profile.html'



class UpdateProfileView(UpdateView):
    model = AcontUser
    template_name = 'editprofile.html'
    form_class = forms.ProfileForm
    success_url = '/profile/'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs= {'pk': self.object.pk})






class DetailFeriasView(DetailView):
    model = AcontUser
    template_name = 'myvacation.html'

class DetailFolgasView(ListView):
    model = Folga
    template_name = 'myrest.html'
    context_object_name = 'folgas'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["folgas"] = Folga.objects.filter(folga_pessoa='1').values()
        return context
    
