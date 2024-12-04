from django.db.models.signals import post_save, pre_save
from aplication.models import Folga, Ferias
from django.dispatch import receiver
from accounts.email_template import solicitacao_folga, aprovacao_folga



@receiver(post_save,sender=Folga)
def post_save(sender,created,instance,**kargs):
    
    if created:
        solicitacao_folga(instance)


    if instance.status_folga == 'APROVADO':
        print('aqui foi aprovado')
        aprovacao_folga(instance)


