from tokenize import generate_tokens
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.views.generic import View
from django.contrib import messages
from .utils import generate_token,TokenGenerator
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def signup(request):
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            # return HttpResponse("Password incrt")
            messages.warning(request,"Password is Incorrect !")
            return render(request,"authentication/signup.html")
            

        try:
            if User.objects.get(username=email):
                # return HttpResponse("username incrt")
                messages.info(request,"Username is Already Verified!")
                return render(request,"authentication/signup.html")


        except Exception as identifier:
            pass
        user=User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()
        email_subject="Activate Your Account"
        message=render_to_string("authentication/activate.html",{
            'user':user,
            'domain': '127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })
        email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email],)
        email_message.send()
        messages.success(request,"Activate your account by clicking the link below")
        return redirect('/auth/login/')
    return render(request,"authentication/signup.html")

#account activation class for url 
class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not  None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activated Successfully")
            return redirect('/auth/login/')
        return render(request,'authentication/activatefail.html')

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login/')

def handlelogin(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['pass1']
        user=authenticate(username=username, password=password)
            # User is authenticated
        if user is not None:
            login(request,user)
            messages.success(request,"Login Success")
            return redirect("/")
        else:
            messages.error(request,"invalid Credentials")
            return redirect('/auth/login/')
    return render(request,"authentication/login.html")
    

def baseauthh(request):
    return render(request,"authentication/baseauth.html")

