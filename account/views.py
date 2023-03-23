
from base64 import urlsafe_b64decode
from django.http import HttpResponse  
from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth import login, authenticate, get_user_model
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.core.mail import EmailMessage
from account.form import SignupForm

from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm 
 
from django.contrib.auth.models import User

from django.utils import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator 
from django.contrib.auth.tokens import default_token_generator

from account.models import CustomUser
 
 
 
def index(request):
    return render(request, 'index.html')



class TokenGen(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

account_activation_token = TokenGen()


User = get_user_model() 
  
def signup(request):  
    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            # the form has to be saved in the memory and not in DB
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            
            # Générer le token et le stocker dans le champ 'token' de l'utilisateur
            token = default_token_generator.make_token(user)
            user.token = token
            user.save()
            
            
            #This is  to obtain the current cite domain   
            current_site_info = get_current_site(request)  
            mail_subject = 'The Activation link has been sent to your email address'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site_info.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token': token,  
            })  
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])  
            email.send()  
            return HttpResponse('Please proceed confirm your email address to complete the registration')  
    else:  
        form = SignupForm()  
    return render(request, 'register.html', {'form': form})  


def activate(request, uidb64, token):   
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError,User.DoesNotExist):  
        user = None  
    if user is not None and default_token_generator.check_token(user, token):  
        user.is_active = True  
        user.save() 
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        messages.error(request, 'Activation link is invalid or has expired.')
        return redirect('signup')  
    
    
    
def login_request(request):
	if request.method == "post":
		form = AuthenticationForm(request.post)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				messages.info(request, f"You are now logged in as {username}.")
				return redirect(request, "index")
			else:
				error_message = messages.error(request,"Invalid username or password.")
    
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'login.html', {"form":form})