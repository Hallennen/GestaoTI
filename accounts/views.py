from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import AcontUser
from aplication.models import Folga
from aplication.forms import FormsFolga
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
        context = Folga.objects.filter(status_folga = 'APROVADO',folga_pessoa_id=self.request.user)
        extra_context = (Folga.objects.filter(status_folga = 'APROVADO', folga_pessoa_id=self.request.user).count())
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
    model = AcontUser
    http_method_names=['post', 'get']
    template_name = 'myrest.html'
    form_class= FormsFolga
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["folgas"] = Folga.objects.filter(folga_pessoa_id=self.request.user).values().order_by('-date_created')[:8]
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



class teste(TemplateView):
    template_name = 'teste.html'

