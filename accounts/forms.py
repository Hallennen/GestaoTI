from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from accounts.models import AcontUser
from django.contrib.auth.hashers import make_password

class CreateUser(forms.ModelForm):
    class Meta: 
        model = AcontUser
        fields = "__all__"
        # fields = ('user','password','first_name','last_name','birthday','telephone','email','unit','cargo','ramal')


    ## criando hash para salva no banco  
    def clean_password(self):
        password = self.cleaned_data.get('password')
        password = make_password(password)
        return password
        