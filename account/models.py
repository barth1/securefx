from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError, models, router, transaction
from django.utils. translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.


class Plan(models.Model):
    plan_name=models.CharField (max_length=20)
    min_amount=models.IntegerField(default=0)
    max_amount=models.IntegerField(default=0)

    def __str__(self):
        return self.plan_name
    


    


class CryptoDetails (models.Model):
    coin_name=models.CharField(max_length=50)
    coin_image=models.ImageField(upload_to='pics')
    wallet_address=models.CharField(max_length=16)
    wallet_backcode=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.coin_name
    

    
 

class UserProfile(models.Model):
    user=models.OneToOneField(User, related_name= 'user_profile', on_delete=models.CASCADE,  primary_key=True)
    ref_by=models.CharField(max_length=50)
    address=models.CharField(verbose_name=_("Address "), max_length=1024, blank=True, null=True)
    zip_code = models.CharField(max_length=12, blank=True, null=True)
    country=CountryField(blank=True , null=True)
    phone_number=PhoneNumberField(null=False, blank=False, unique=True)
    deposit_wallet=models.DecimalField(max_digits=5, decimal_places=2)
    interest_wallet=models.DecimalField(max_digits=5, decimal_places=2)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.email
    



    

class Investment  (models.Model):
    user= models.ForeignKey(UserProfile, related_name='user_account', on_delete=models.CASCADE)
    amount=models.IntegerField()
    coin_deposit= models.ForeignKey(CryptoDetails, related_name='invest_crypto', on_delete=models.CASCADE)
    investment_plan=models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='user_plan')
    investment_date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)


    def __unicode__(self):
        return self.user

class Withdrawal (models.Model):
    user=models.ForeignKey(UserProfile, related_name='withdraw', on_delete=models.CASCADE)
    amount=models.IntegerField()
    coin=models.ForeignKey(CryptoDetails, related_name='withdraw_coin', on_delete=models.CASCADE)



   
    

    
  

    


    









    










