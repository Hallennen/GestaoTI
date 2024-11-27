from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from accounts.models import AcontUser
from django.contrib.auth.hashers import make_password


@receiver(pre_save,sender=AcontUser)
def pre_save(sender,instance, **kwargs):
    num = AcontUser.objects.filter(pk=instance.pk).count()
    if num > 0: 
        instance.password = make_password(instance.password)
            

        return instance.password    
    

    

    