from django.db import models
from accounts.models import AcontUser, Unit

# Create your models here.
MOTIVOS_FOLGA =[('DOMINGO TRABALHADO','TRABALHADO',),
        ('COMBINADO GESTOR','COMBINADO',), 
        ('OUTROS','OUTROS'),           
    ]

STATUS_FOLGA = [
    ('PENDENTE','PENDENTE'),
    ('APROVADO','APROVADO'),
    ('RECUSADO','RECUSADO'),
    ]


class Folga(models.Model):
    day = models.DateField(unique= True)
    motivo = models.CharField(choices = MOTIVOS_FOLGA, max_length= 25 )
    date_created = models.DateField(auto_now_add= True, null= True)
    date_updated = models.DateField(null=True, blank=True)
    folga_pessoa = models.ForeignKey(AcontUser, on_delete=models.CASCADE ,related_name='folga_pessoa')
    status_folga = models.CharField(choices= STATUS_FOLGA, default='PENDENTE',max_length= 25)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT,related_name='folga_unidade')
    observacao = models.TextField(max_length=250, null=True, blank=True, verbose_name='Observação:')

    def __str__(self):
        return str(self.day)