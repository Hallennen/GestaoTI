from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from accounts.models import AcontUser
from django.contrib.auth.hashers import make_password
from aplication.utilites import correcao_url


@receiver(pre_save,sender=AcontUser)
def pre_save(sender,instance, **kwargs):
    num = AcontUser.objects.filter(pk=instance.pk).count()

    if num == 0 and AcontUser.objects.filter(pk=instance.pk).exists() == False: 
        instance.password = make_password(instance.password)
        print('salvo no banco')
        print('criptografo')

        return instance.password   


    if instance.path:

        if '\\' in instance.path:
            path = correcao_url(instance.path)
            instance.path = path    

            return instance.path



    