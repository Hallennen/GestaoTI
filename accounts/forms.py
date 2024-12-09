from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from accounts.models import AcontUser
from django.contrib.auth.hashers import make_password
from aplication import utilites

class CreateUser(forms.ModelForm):
    class Meta: 
        model = AcontUser
        fields = "__all__"

    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = AcontUser
        fields = ['photo','username','first_name','last_name','birthday','telephone','email','ramal', 'unit','photo','path']  

            
    def clean_photo(self):

        return self.cleaned_data['photo']
 




