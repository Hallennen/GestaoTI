from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from accounts.models import User

# class CreateUser(forms.ModelForm):
#     class Meta: 
#         model = User
#         fields = ('user','password','first_name','last_name','birthday','telephone','email','unit','cargo','ramal')