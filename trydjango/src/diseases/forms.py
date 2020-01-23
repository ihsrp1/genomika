from django import forms

from .models import Disease
from .models import User_two

class DiseaseModelForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = [
            'name'
        ]
        labels = {
            'name': ''
        }

class UserModelForm(forms.Form):
    username = forms.CharField(max_length=60, label='Usuário')
    password = forms.CharField(max_length=60, widget=forms.PasswordInput, label='Senha')

class SignupModelForm(forms.ModelForm):
    class Meta:
        model = User_two
        fields = [
            'username',
            'password'
        ]
        labels = {
            'username': 'Usuário',
            'password': 'Senha'
        }
        