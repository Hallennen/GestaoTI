from django import forms
from aplication.models import Folga
from accounts.models import AcontUser
from aplication.models import Unit
from django.core.exceptions import ValidationError
import datetime


MOTIVOS_FOLGA =[('DOMINGO TRABALHADO','DOMINGO TRABALHADO'),
        ('COMBINADO GESTOR','COMBINADO GESTOR'),  
        ('OUTROS','OUTROS')          
    ]

STATUS_FOLGA = [
    ('PENDENTE','PEN'),
    ('APROVADO','APR'),
    ('RECUSADO','REC'),
    ]

DIAS_SEMANA = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]



class FormsFolga(forms.Form):
    Dia = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    Motivo = forms.ChoiceField(choices=MOTIVOS_FOLGA)
    Observação = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":"4", "required":"False"}))


    def clean_Dia(self):
        dia = self.cleaned_data.get('Dia')
        data_separado= str(dia).split('-')
        ANO = int(data_separado[0])
        MES = int(data_separado[1])
        DIA = int(data_separado[2])
        print(ANO)
        print(MES)
        print(DIA)


        dia_da_semana = datetime.date(year=ANO, month=MES, day=DIA)
        print(type(dia_da_semana.isoweekday()))

        data_atual = datetime.date.today()
        folga_aprovada = Folga.objects.filter(day = dia, status_folga="APROVADO")
        folga_pendente = Folga.objects.filter(day = dia, status_folga="PENDENTE")
        if (folga_aprovada or folga_pendente):
            raise ValidationError(    [
                ("O dia selecionado já possui solicitação pendente para o gestor ou está aprovada."),
                ("Verifique o calendário"),
            ])
        
        if dia < data_atual:
            print('menor')
            raise ValidationError(    [
                (f"Não é possivel fazer solicitação com uma data inferior a data de hoje ({data_atual})"),
            ])
    
        if (dia_da_semana.isoweekday() == 6 or dia_da_semana.isoweekday() == 7):
            raise ValidationError(    [
                (f"Só é possivel fazer solicitação em dias da semana (segunda - sexta)."),
            ])

        


    
        
        
    


    def save(self, pk, unit):
        instance = self
        folga = Folga(
            day= instance['Dia'],
            motivo = instance['Motivo'],
            folga_pessoa = AcontUser.objects.get(pk= pk),
            status_folga = 'PENDENTE',
            unit = Unit.objects.get(pk= unit),
            observacao = instance['Observação'],
        )
        folga.save()

        return print('salvo')


        # formfolga.save()
        # return formfolga