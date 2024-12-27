from django.db.models.signals import post_save, pre_save
from aplication.models import Folga, Ferias
from accounts.models import AcontUser
from django.dispatch import receiver
from accounts.email_template import solicitacao_folga, aprovacao_folga



@receiver(post_save,sender=Folga)
def post_save(sender,created,instance,**kargs):
    
    if created:
        try:
            solicitacao_folga(instance)
        except:
            ...
        update_saldo_folga(instance.folga_pessoa.id, 'menos')


    if instance.status_folga == 'APROVADO':
        try:
            aprovacao_folga(instance)
        except:
            ...

    if instance.status_folga ==  'RECUSADO':
        update_saldo_folga(instance.folga_pessoa.id, 'mais')


def update_saldo_folga(user,operacao=['mais', 'menos']):
    pessoa = AcontUser.objects.filter(pk = user)
    saldo_folga = pessoa.values('saldo')[0]['saldo']
    if operacao == 'menos':
        novo_saldo = saldo_folga -1
    elif operacao == 'mais':
        novo_saldo = saldo_folga +1
    
    return pessoa.update(saldo = novo_saldo)


