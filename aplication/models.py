from django.db import models
from accounts.models import AcontUser
# Create your models here.
MOTIVOS_FOLGA =[('DOMINGO TRABALHADO','TDM',),
        ('COMBINADO GESTOR','CCG',),            
    ]

STATUS_FOLGA = [
    ('PENDENTE','PEN'),
    ('APROVADO','APR'),
    ('RECUSADO','REC'),
    ]


class Folga(models.Model):
    day = models.DateField()
    motivo = models.CharField(choices = MOTIVOS_FOLGA, max_length= 25 )
    folga_pessoa = models.ForeignKey(AcontUser, on_delete=models.PROTECT ,related_name='folga_pessoa')
    status_folga = models.CharField(choices= STATUS_FOLGA, default='PENDENTE',max_length= 25)

    def __str__(self):
        return str(self.day)