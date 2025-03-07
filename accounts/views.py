from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import AcontUser
from aplication.models import Folga, Ferias
from aplication.forms import FormsFolga
from accounts import forms
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView,ListView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from accounts.email_template import reset_senha
import random
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import datetime


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None :
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


def recuperacao_senha(request):
    if request.method == 'GET':
        return render(request,'recuperacao_senha.html')
    if request.method == 'POST':
        email = request.POST['email']

        if AcontUser.objects.filter(email= email).exists():
            lista = "abcdefghijklmnopqrstuvwxyz123456789!@##$%&*()_+ABCDEFGHIJLMNOPQRSTUVZXYW"
            senha = "".join(random.sample(lista,8))  
            senha_hash = make_password(senha)
            AcontUser.objects.filter(email= email).update(password = senha_hash)
            
            reset_senha(email,senha)

            return render(request,'recuperacao_senha.html',{'messages_positiva':'E-mail enviado'})
        else:
            return render(request,'recuperacao_senha.html',{'messages':'nenhum email encontrado'})









@method_decorator(login_required(login_url='login'), name='dispatch')
class AplicationView(TemplateView):
    template_name = 'aplication.html'   


    def get_context_data(self, **kwargs):
        context = Folga.objects.filter(status_folga = 'APROVADO')
        context_pendente = Folga.objects.filter(status_folga = 'PENDENTE', day__gte=(datetime.date.today()))
        folgas = Folga.objects.filter(folga_pessoa_id=  self.request.user,status_folga = 'APROVADO')
        extra_context = (Folga.objects.filter(status_folga = 'APROVADO', folga_pessoa_id=self.request.user).count())
        return ({'context':context, 'contadores':extra_context, 'folgas':folgas, 'context_pendente':context_pendente})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateProfile(CreateView):
    model = AcontUser
    template_name = 'createprofile.html'
    form_class = forms.CreateUser
    success_url = '/listprofile/'



@method_decorator(login_required(login_url='login'), name='dispatch')
class DetailProfileView(DetailView):
    model = AcontUser
    template_name = 'profile.html'

    def post(self, request, **kwargs):
        pk = kwargs.get('pk')
        senha1 = request.POST['password1']
        senha2 = request.POST['password2']
        if senha1 == senha2:
            senha1 = make_password(senha1)
            AcontUser.objects.filter(pk=pk).update(password=senha1)

            return redirect ('login')



@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateProfileView(UpdateView):
    model = AcontUser
    template_name = 'editprofile.html'
    form_class = forms.ProfileForm
    success_url = '/profile/'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs= {'pk': self.object.pk})








@method_decorator(login_required(login_url='login'), name='dispatch')
class DetailFeriasView(ListView):
    model = Ferias
    template_name = 'myvacation.html'



    def get_context_data(self, **kwargs):
        ferias = super().get_context_data(**kwargs)
        ferias['ferias'] =  Ferias.objects.filter(pessoa_vacation_id = self.request.user, start_vacation__gte =(datetime.date.today()))

        
        return ferias
    





@method_decorator(login_required(login_url='login'), name='dispatch')
class DetailFolgasView(ListView):
    model = AcontUser
    http_method_names=['post', 'get']
    template_name = 'myrest.html'
    form_class= FormsFolga
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["folgas"] = Folga.objects.filter(folga_pessoa_id=self.request.user).values().order_by('-date_created')[:10]
        context["aprovadas"] = Folga.objects.filter(folga_pessoa_id=self.request.user, status_folga= 'APROVADO').count()
        context["pendentes"] = Folga.objects.filter(folga_pessoa_id=self.request.user, status_folga= 'PENDENTE').count()
        context["recusadas"] = Folga.objects.filter(folga_pessoa_id=self.request.user, status_folga= 'RECUSADO').count()
        context['forms'] = self.form_class
        context['error_sem_folga'] = 'Sem Folga'
        return (context)


    
    def post(self, request,**kwargs):
        pk = kwargs.get('pk')
        unidade = AcontUser.objects.filter(pk=pk).values('unit')
        unit = unidade[0]['unit']
        new_form = FormsFolga(request.POST)
        if new_form.is_valid():
            FormsFolga.save(request.POST,pk,unit)
            return redirect ('rest', pk=pk)
        else:
            context = {}
            context["folgas"] = Folga.objects.filter(folga_pessoa_id=self.request.user).values().order_by('-date_created')[:8]
            context["aprovadas"] = Folga.objects.filter(folga_pessoa_id=self.request.user, status_folga= 'APROVADO').count()
            context["pendentes"] = Folga.objects.filter(folga_pessoa_id=self.request.user, status_folga= 'PENDENTE').count()
            context["recusadas"] = Folga.objects.filter(folga_pessoa_id=self.request.user, status_folga= 'RECUSADO').count()
        
            return render(request, 'myrest.html', {'notificacao':new_form.errors,'forms':self.form_class,'aprovadas':context['aprovadas'],
                                                   'pendentes':context['pendentes'],'recusadas':context['recusadas'],'folgas':context['folgas']})
                  
    
        # username =  AcontUser.objects.filter(pk=pk).values('username')[0]['username']
        # user = request.user


