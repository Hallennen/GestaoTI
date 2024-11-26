from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView,DetailView
from .models import Folga, Unit
from accounts.models import AcontUser
from aplication.forms import FolgasFormUpdate
from django.urls import reverse_lazy
import pandas as pd


from  datetime import datetime

# Create your views here.
class ViewSolicitacao(ListView):
    model = Folga
    template_name = 'viewsolicitacao.html'
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folgas'] = Folga.objects.filter(status_folga='PENDENTE').order_by('date_created')
        

        return context
    


class EditSolicitacao(UpdateView):
    model = Folga
    template_name = 'EditSolicitacao.html'
    form_class = FolgasFormUpdate
    success_url = '/solicitacao/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folgas'] = Folga.objects.filter(status_folga='PENDENTE')
    
        return context
    

    def get_success_url(self):
        return reverse_lazy('viewsolicitacao',)




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
                                    
        arquivo = open(f'relatorio{dta_of}-{dta_at}','+a', encoding='utf-8')
        arquivo.write(f'PERIODO: {str(dta_of)} á {str(dta_at)}\n\nDT_FOLGA;MOTIVO;DT_CRIAÇÃO;STATUS;TECNICO;UNIDADE \n')
        # arquivo.write(str(folga.values()))
        for folg in folga:
            arquivo.write(f'{folg.day};{folg.motivo};{folg.date_created};{folg.status_folga};{folg.folga_pessoa};{folg.unit}\n')
        
        alerta = 'Relatório gerado' 


        return render(request,'viewgeral.html',{'alerta':alerta,'folgas':folga,'unidades':unidades, 'tecnicos':tecnicos})
    


class ViewRouter(ListView):
    model = Folga
    template_name = 'routers.html'
    context_object_name = 'routers'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routers'] = Folga.objects.filter(status_folga = 'APROVADO').order_by('day')
        date_of= self.request.GET.get('date_of')
        date_at= self.request.GET.get('date_at')


        if(date_at and date_of):
            context['routers'] = Folga.objects.filter(day__range = (date_of, date_at), status_folga = 'APROVADO').order_by('day')

        return context
    