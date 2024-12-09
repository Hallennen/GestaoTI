from django.db.models.signals import pre_save
from aplication.models import Ferias
from django.dispatch import receiver


@receiver(pre_save,sender=Ferias)
def pre_save(sender,instance,**kargs):
    data = instance.start_vacation
    data = data.strftime("%B")
    instance.month = data
