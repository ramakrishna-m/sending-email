from django.core.mail import send_mail
from django.shortcuts import render
from sendemail import settings


def index(request):
    return render(request,'index.html')


def sendingmail(request):
    h=request.POST.get("email")
    subject="hi how r u"
    From_email=settings.EMAIL_HOST_USER
    to_email=[h]
    mes="i am ramakrishna"
    send_mail(subject=subject,from_email=From_email,recipient_list=to_email,message=mes,fail_silently=False)
    return render(request,'email.html')
