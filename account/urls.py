from django.urls import path, include
from django.conf.urls import url
from . import views
# from account.views import SignUpView, ActivateAccount, ProfileView
# from django_email_verification  import urls as mail_urls

app_name='account'

urlpatterns = [
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', views.accountProfile, name='accounts'),
    path('deposit/', views.deposit, name='deposit'),
    path('cyptocurrency/', views.cryptocurrency, name='cryptocurrency'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('transactions/', views.transactions, name='transactions'),
    path('referrals/', views.referrals, name='referrals'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.register, name='signup'),
    path('signout/', views.logout_user, name='signout'),
    path('invest/', views.investment, name='invest'),
    path('preview/', views.payment_preview, name='preview'),
    path('confirm/', views.confirm_deposit, name='confirm'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        # views.activate_account, name='activate'),
    
    # path('emails/',include('mail_urls')),

]