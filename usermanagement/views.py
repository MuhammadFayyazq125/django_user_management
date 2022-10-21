from django.shortcuts import render
from .forms import CustomaccountFrom
from .models import designation
from django.urls import reverse_lazy
import requests
from django.views.generic.edit import CreateView
from django.contrib.sites.shortcuts import get_current_site  
from django.template.loader import render_to_string  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from .token import account_activation_token 
from django.core.mail import EmailMessage  
from django.utils.encoding import force_bytes , smart_str
from django.http import HttpResponse 
from .models import Account   








# Create your views here.
# class Signup(CreateView):
#     form_class=CustomaccountFrom
#     success_url=reverse_lazy('login')
#     template_name='signup.html'

def send_mail(send_from,send_to,subject,cc,bcc,htmlBody,password):
    url = 'https://mis.mobilelinkusa.com/MLServiceAPI/api/SendEmail/SendEmailBody/'
    data = {"from": send_from, "to":send_to,"subject": subject,'cc':cc,'bcc':bcc,'htmlBody':htmlBody,'password':password}
    response = requests.post(url, json=data)


# send_mail('hasan_khan@mobilelinkusa.com','danish_hussain@mobilelinkusa.com',
        # 'testing subject','haseeb_ahmed@mobilelinkusa.com','',
        # 'testing body via py file','mobilelink@2')

def signup(request):
    if request.method=='POST':
        form = CustomaccountFrom(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
             # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email') 
            print (to_email) 
            send_mail('hasan_khan@mobilelinkusa.com',to_email,mail_subject,'','',message,'mobilelink@2') 
            return HttpResponse('Please confirm your email address to complete the registration')  
    else:  
        form = CustomaccountFrom()  
    return render(request, 'signup.html', {'form': form})  

def activate(request, uidb64, token):  
  
    # try:  
    uid = smart_str(urlsafe_base64_decode(uidb64))
    print("uid ======================== ",uid)
    user = Account.objects.get(pk=uid)
    print("user =============================== ", user) 
    # except(TypeError, ValueError, OverflowError, Account().DoesNotExist):  
    #     user = None

    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    # else:  
    #     print(user,'user======')
    #     return HttpResponse('Activation link is invalid!')  
def home(request):
    return render(request,'home.html')
    

