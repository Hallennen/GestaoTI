from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView,DetailView, CreateView
from .models import Folga, Unit
from accounts.models import AcontUser
from aplication.models import Ferias
from aplication.forms import FolgasFormUpdate, FeriasCreateForm
from django.urls import reverse_lazy
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import datetime



# Create your views here.
class ListProfile(ListView):
    model = AcontUser
    template_name = 'listprofile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        profile = super().get_context_data(**kwargs) 
        profile['profile'] = AcontUser.objects.all().order_by('first_name')

        return profile





@method_decorator(login_required(login_url='login'), name='dispatch')
class ViewSolicitacao(ListView):
    model = Folga
    template_name = 'viewsolicitacao.html'
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folgas'] = Folga.objects.filter(status_folga='PENDENTE', day__gte=(datetime.date.today())).order_by('day')
        

        return context
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class EditSolicitacao(UpdateView):
    model = Folga
    template_name = 'editsolicitacao.html'
    form_class = FolgasFormUpdate
    success_url = '/solicitacao/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folgas'] = Folga.objects.filter(status_folga='PENDENTE')
    
        return context
    

    def get_success_url(self):
        return reverse_lazy('viewsolicitacao',)



@method_decorator(login_required(login_url='login'), name='dispatch')
class ViewGeral(ListView):
    model = Folga
    template_name = 'viewgeral.html'
    paginate_by = 10
    context_object_name = 'folgas'

    def get_queryset(self):
        folgas = super().get_queryset().order_by('unit')
        search = self.request.GET.get('search')
        search_name = self.request.GET.get('search-name')
        search_status = self.request.GET.get('search_status')
        search_date = self.request.GET.get('search_date')
 
        if search :
            folgas = Folga.objects.filter(unit = search)
        elif search_name :
            folgas = Folga.objects.filter(folga_pessoa = search_name)

        elif search_status: 
            folgas = Folga.objects.filter(status_folga = search_status)
        elif search_date: 
            folgas = Folga.objects.filter(day = search_date).order_by('status_folga')

        return folgas
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unidades'] = Unit.objects.all().order_by('name_unit')
        context['tecnicos'] = AcontUser.objects.all()

        return context
    
    def post(self, request,**kwargs):
        unidades = Unit.objects.all().order_by('name_unit')
        tecnicos = AcontUser.objects.all()
        

        folga = Folga.objects.filter(day__range= (self.request.POST['date_for'], self.request.POST['date_at']),)

        if not self.request.POST['tec'] and  not self.request.POST['unit']:
            folga = Folga.objects.filter(day__range= (self.request.POST['date_for'], self.request.POST['date_at']))

        elif self.request.POST['tec'] and self.request.POST['unit']:
            folga = Folga.objects.filter(day__range= (self.request.POST['date_for'], self.request.POST['date_at']),
                                         unit= self.request.POST['unit'],folga_pessoa= self.request.POST['tec']   )

        elif self.request.POST['tec']:
            folga = Folga.objects.filter(day__range= (self.request.POST['date_for'], self.request.POST['date_at']),
                                         folga_pessoa= self.request.POST['tec'] )

        elif self.request.POST['unit']:
            folga = Folga.objects.filter(day__range= (self.request.POST['date_for'], self.request.POST['date_at']),
                                         unit= self.request.POST['unit'] )


        dta_of = self.request.POST['date_for']
        dta_at = self.request.POST['date_at']

       
        path = AcontUser.objects.filter(pk = self.request.user.id).values('path')
        try:
            path_ajustado =path[0]['path']
            arquivo = open(f"{path_ajustado}relatorio{dta_of}-{dta_at}",'+a', encoding='utf-8')
            arquivo.write(f'PERIODO: {str(dta_of)} á {str(dta_at)}\n\nDT_FOLGA;MOTIVO;DT_CRIAÇÃO;STATUS;TECNICO;UNIDADE \n')
            for folg in folga:
                arquivo.write(f'{folg.day};{folg.motivo};{folg.date_created};{folg.status_folga};{folg.folga_pessoa};{folg.unit}\n')
            
            alerta = 'Relatório gerado' 
            return render(request,'viewgeral.html',{'alerta':alerta,'folgas':folga,'unidades':unidades, 'tecnicos':tecnicos})
        except:

            alerta = ' Não foi possivel salvar o relatório, verifique o path salvo '

            return render(request,'viewgeral.html',{'alerta_negativo':alerta,'folgas':folga,'unidades':unidades, 'tecnicos':tecnicos})
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class ViewRouter(ListView):
    model = Folga
    template_name = 'routers.html'
    context_object_name = 'routers'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routers'] = Folga.objects.filter(status_folga = 'APROVADO', day__gte=(datetime.date.today())).order_by('day')
        date_of= self.request.GET.get('date_of')
        date_at= self.request.GET.get('date_at')


        if(date_at and date_of):
            context['routers'] = Folga.objects.filter(day__range = (date_of, date_at), status_folga = 'APROVADO').order_by('day')

        return context
    



class VacationView(CreateView):
    model = Ferias
    template_name = 'listvacation.html'
    form_class= FeriasCreateForm
    success_url = '/ferias/'
    contect_object_name = 'feriass'

    def get_context_data(self, **kwargs):
        ferias = super().get_context_data(**kwargs)
        # anos = Ferias.objects.all().values('year').distinct().values('year')
        # ferias['feriass'] = Ferias.objects.all() 

        ferias = Ferias.objects.all().order_by('start_vacation__year')
        ferias_por_ano= {}
        for f in ferias:
            ano = f.start_vacation.year
            ferias_por_ano.setdefault(ano, []).append(f)

        print(ferias_por_ano)
        return {'ferias_ano':ferias_por_ano, 'form':FeriasCreateForm}
    
def DeleteFeriasView(request,pk):
    Ferias.objects.filter(id=pk).delete()
    print('item excluido')
    return redirect('vacation_list')