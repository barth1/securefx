from django.urls import path
from . import views

app_name='frontend'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('plans/', views.plans, name='plans'),
    path('support/', views.support, name='support'),
    path('terms/', views.terms, name='terms'),

]