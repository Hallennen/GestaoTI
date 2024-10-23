from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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




POSITIONS = (
    ('Gestor','Gestor-T.I'),
    ('T.I','Técnico-T.I'),
)

class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)
    def create_user(self, user, password = None, is_active = True, is_staff = False, is_admin = False):
        if not user:
            raise ValueError("O Usuário deve ter um user.")
        if not password:
            raise ValueError("O Usuário deve ter uma senha.")
        user_obj = self.model(
            email = self.normalize_email(user)
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


class User(AbstractBaseUser):

    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    user = models.CharField(unique=True, max_length=7)
    birthday = models.DateField(default= '1999-01-01')
    telephone = models.CharField(max_length=13, blank=True)
    email = models.EmailField(default='email_default@email.com')
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, related_name='unit_account',null=True, default=1)
    ramal = models.CharField(max_length=9, null=True)
    cargo = models.CharField(null=True, blank=True, default='T.I-Tecnico')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.user


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



