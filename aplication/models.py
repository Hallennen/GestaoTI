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
    day = models.DateField()
    motivo = models.CharField(choices = MOTIVOS_FOLGA, max_length= 25 )
    date_created = models.DateField(auto_now_add= True, null= True)
    date_updated = models.DateField(null=True, blank=True)
    folga_pessoa = models.ForeignKey(AcontUser, on_delete=models.CASCADE ,related_name='folga_pessoa')
    status_folga = models.CharField(choices= STATUS_FOLGA, default='PENDENTE',max_length= 25)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT,related_name='folga_unidade')
    observacao = models.TextField(max_length=50, null=True, blank=True, verbose_name='Observação:')

    def __str__(self):
        return f'{self.day}'
    


class Ferias(models.Model):
    pessoa_vacation = models.ForeignKey(AcontUser,on_delete= models.CASCADE, related_name = 'ferias_pessoa', verbose_name='Colaborador')
    start_vacation = models.DateField(unique = True, verbose_name='Data inicio:')
    end_vacation = models.DateField(verbose_name="Data Fim")
    month = models.CharField(default='',blank= True)
    unit = models.ForeignKey(Unit, on_delete= models.CASCADE, related_name='ferias_unidade',verbose_name='Unidade')

    def __str__(self):
        return self.pessoa_vacation.get_full_name()