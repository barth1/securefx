from django.contrib import admin
from .models import UserProfile, CryptoDetails, Plan, Investment, Withdrawal

admin.site.register(UserProfile)
admin.site.register(Investment)
admin.site.register(Plan)
admin.site.register(CryptoDetails)
admin.site.register(Withdrawal)