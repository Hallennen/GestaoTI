from django.db import models

# Create your models here.
LOGRADOURO = (
    ('Rua','Rua'),
    ('AV','Avenida'),

)

class Unit(models.Model):
    name_unit = models.CharField(max_length=60)
    logradouro = models.CharField(choices = LOGRADOURO, max_length=50,blank=True, null=True)
    adress = models.CharField(max_length=120)
    number_adress = models.IntegerField(blank= True)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.name_unit




# POSITIONS = (
#     ('Gestor','Gestor-T.I'),
#     ('T.I','Técnico-T.I'),
# )


# class Accounts(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     user = models.CharField(unique=True, max_length=7)
#     birthday = models.DateField()
#     telephone = models.CharField(max_length=13)
#     email = models.EmailField()
#     unit = models.ForeignKey(Unit, on_delete=models.PROTECT, related_name='unit_account')
#     ramal = models.CharField(max_length=9)
#     cargo = models.Choices(choices= POSITIONS)


#     def __str__(self):
#         return self.first_name