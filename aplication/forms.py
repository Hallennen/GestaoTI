from django import forms
from aplication.models import Folga
from accounts.models import AcontUser
from aplication.models import Unit


MOTIVOS_FOLGA =[('DOMINGO TRABALHADO','DOMINGO TRABALHADO'),
        ('COMBINADO GESTOR','COMBINADO GESTOR'),            
    ]

STATUS_FOLGA = [
    ('PENDENTE','PEN'),
    ('APROVADO','APR'),
    ('RECUSADO','REC'),
    ]





class FormsFolga(forms.Form):
    day= forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    # day= forms.DateField(attrs={'type':'date'})
    motivo = forms.ChoiceField(choices=MOTIVOS_FOLGA)



    def save(self, pk, unit):
        instance = self
        folga = Folga(
            day= instance['day'],
            motivo = instance['motivo'],
            folga_pessoa = AcontUser.objects.get(pk= pk),
            status_folga = 'PENDENTE',
            unit = Unit.objects.get(pk= unit)
        )
        folga.save()

        return print('salvo')


        # formfolga.save()
        # return formfolga