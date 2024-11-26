from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
LOGRADOURO = (
    ('Rua','Rua'),
    ('AV','Avenida'),
    ('ES','Estrada'),

)

class Unit(models.Model):
    name_unit = models.CharField(max_length=60)
    logradouro = models.CharField(choices = LOGRADOURO, max_length=50,blank=True, null=True)
    adress = models.CharField(max_length=120)
    number_adress = models.IntegerField(blank= True)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.name_unit






class UserManager(BaseUserManager):
    def get_by_natural_key(self, user):
        return self.get(user=user)
    def create_user(self, user, password = None, is_active = True, is_staff = False, is_admin = False):
        if not user:
            raise ValueError("O Usuário deve ter um user.")
        if not password:
            raise ValueError("O Usuário deve ter uma senha.")
        user_obj = self.model(
            user = self.normalize_user(user)
        )
        user_obj.set_password(password) # muda a senha
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, user, password = None):
        user = self.create_user(
            user,
            password = password,
            staff = True
        )
        return user
    def create_superuser(self, user, password = None):
        user = self.create_user(
            user,
            password = password,
            is_staff = True,
            is_admin = True,
        )
        return user


# POSITION= (
#     ('Gestor','Gestor-T.I'),
#     ('T.I','Técnico-T.I'),
#     ('T.I-V', 'Volante'),
# )

class Position(models.Model):
    position_name = models.CharField(max_length=25)

    def __str__(self):
        return self.position_name


class AcontUser(AbstractUser):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    user = models.CharField(unique=True, max_length=7)
    birthday = models.DateField(default= '1999-01-02')
    telephone = models.CharField(max_length=13, blank=True)
    email = models.EmailField(default='email_default@email.com')
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, related_name='unit_account',null=True)
    ramal = models.CharField(max_length=9, null=True)
    cargo = models.ForeignKey(Position, on_delete=models.PROTECT, related_name='position_account', null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to= 'profile/', blank=True, null=True,  verbose_name = "Foto")

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.first_name +' '+ self.last_name


    def get_full_name(self):
        return (self.first_name + self.last_name) 
    
    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, object=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_activate(self):
        return self.active
    # @property
    # def password(self):
    #     password = make


