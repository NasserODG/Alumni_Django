from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text
from Alumni_app.tokens import generatorToken
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User


from django.shortcuts import render

from django.db.models import Q
from django.core.validators import validate_email
from connexion.models import Etudiant
from Alumni_app import settings
from django.core.mail import send_mail,EmailMessage

# Create your views here.
def home (request):
    return render (request, 'register.html')
def sign_up(request):
    error =False
    message=""
    if request.method=='POST':
        first_name = request.POST.get('first_name',None)
        last_name = request.POST.get('last_name',None)
        email= request.POST.get('email',None)
        phone=request.POST.get('phone',None)
        password=request.POST.get('password',None)
        repassword=request.POST.get('repassword',None)  
        
        try:
           validate_email(email)
        except: 
            error=True
            message ="Entrez un email valide"
        if error==False:
            if password != repassword:
                error=True
                message ="les deux mots de passe ne correspond pas "
        if error==False:
             etudiant= Etudiant.objects.filter(Q(email=email)|Q(last_name=last_name)).first()
             
             if etudiant:
                error=True
                message =f"un utilisateur avec ce first_name {first_name} email {email} existe deja"  
        if error==False:
            if  'agree' not in request.POST :
                error=True
                message =" veillez accepter les terme d'utilisation "
        
        
        
        
        if error==False:
            etudiant = Etudiant (
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone,
            
            )
            etudiant.mot_de_passe=password
            subject ='Bienvenu sur Alumni IBAM'
            message= "Bienvenu "+ etudiant.first_name +" "+etudiant.last_name+ "\n\n\n nous sommes heureux de vous compter parmis vous \n\n\n By habib pro dev"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [etudiant.email]
            send_mail(subject,
            message,
            from_email,
            recipient_list)
            etudiant.save()
            # email de confirmation 
            current_site = get_current_site(request)
            email_subject = "confirmation de votre email sur Alumni IBAM"
            email_message =render_to_string('confirmation.html',{
                'name': etudiant.first_name,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(etudiant.pk)),
                'token':generatorToken.make_token(etudiant)
            })
            email=EmailMessage(email_subject,email_message,settings.EMAIL_HOST_USER,[etudiant.email])
            email.send()
    context={
        'error':error,
        'message':message
    }
    return render(request, 'register.html',context)
def sign_in(request):
    return render(request,'sing_in.html')
def log_out(request):
    return render(request,'log_out.html')
def activate (request,uidb64,token):
    
    try:
        uid= force_text(urlsafe_base64_decode(uidb64))
        user = Etudiant.objects.get(pk=uid)
    except(TypeError,ValueError,Etudiant.DoesNotExist):
        user=None
    
    if user is not None and generatorToken.check_token(user, token):
        user.is_active=True
        user.save()
    else:
        print("nous pouvons pas activer votre compte")