from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import UserProfile, Investment
from django.forms import HiddenInput

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=250)
    last_name=forms.CharField(max_length=250)  
    email=forms.EmailField(label='Email Address', required=True)
    class Meta:
        model=User
        fields=('first_name','last_name','username','email', 'password1','password2')



class MakeInvestment(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ( 'amount', 'coin_deposit')
        widgets={
            'coin_deposit':forms.HiddenInput()
        }
