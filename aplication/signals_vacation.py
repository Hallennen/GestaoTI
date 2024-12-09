from django.db.models.signals import pre_save
from aplication.models import Ferias
from django.dispatch import receiver


@receiver(pre_save,sender=Ferias)
def pre_save(sender,instance,**kargs):
    data_ferias = instance.start_vacation
    mes = data_ferias.strftime("%B")
    ano = data_ferias.strftime("%Y")
    instance.month = mes
    instance.year = ano

