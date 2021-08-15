from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.form import SignUpForm, MakeInvestment
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from account.tokens import account_activation_token
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.http import HttpResponse
import uuid
from django.contrib import messages
from django.db.models.query_utils import Q
from .models import CryptoDetails, Investment, Plan, UserProfile



@login_required
def dashboard (request): 
    diction={}
    return render(request, 'account/dashboard.html', context=diction)


@login_required
def investment (request):
    form=Plan.objects.all()
    diction={'form':form}
    return render(request, 'account/investment.html', context=diction)

@login_required
def accountProfile (request):
    diction={}
    return render(request, 'account/account.html', context=diction)

@login_required
def cryptocurrency (request):
    form=CryptoDetails.objects.all()
    diction={'form':form}
    return render(request, 'account/deposit.html', context=diction)
@login_required
def deposit (request):
    form=MakeInvestment()
    if request.method=='POST':
        form=MakeInvestment(request.POST)
        if form.is_valid:
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('account:preview'))
        else:
            return HttpResponseRedirect(reverse('account:cryptocurrency'))
    diction={'form':form}
    return render(request, 'account/deposit.html', context=diction)

@login_required
def withdraw (request):
    diction={}
    return render(request, 'account/withdraw.html', context=diction)

@login_required
def transactions (request):
    diction={}
    return render(request, 'account/transactions.html', context=diction)

@login_required
def referrals (request):
    diction={}
    return render(request, 'account/referrals.html', context=diction)

@login_required
def profile (request):
    diction={}
    return render(request, 'account/profile.html', context=diction)

@login_required
def confirm_deposit (request):
    form=CryptoDetails.objects.all()
    diction={'form':form}
    return render(request, 'account/deposit_confirm.html', context=diction)

@login_required
def payment_preview (request):
    deposits=CryptoDetails.objects.all()
    diction={'deposits':deposits}
    return render(request, 'account/payment_Preview.html', context=diction)


def login_page (request):
    form=AuthenticationForm()
    if request.method =='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('account:dashboard'))
    return render(request, 'account/login.html', context={'form':form})

@csrf_exempt
def register (request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('account/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            messages.info(request, "We have sent an email, please confirm your email address to complete registration")
            return HttpResponseRedirect(reverse('account:login')) 
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})



def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, "Your email as been validated!")
        return HttpResponseRedirect(reverse('account:dashboard'))
       
    else:
        messages.error(request, "Activation link is invalid")
        return HttpResponseRedirect(reverse('account:signup'))
        

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('frontend:home'))


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "account/create_password_reset_email.html"
					c = {
					"email":user.email,
					'domain':'http://mydomain.com/',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
						
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return HttpResponseRedirect(reverse('account:login'))
                   
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="account/reset_password.html", context={"password_reset_form":password_reset_form})
