from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

from django_send_app.settings import EMAIL_HOST_USER
from django.conf import settings
from twilio.rest import Client

import zerosms
import twilio
import twilio
import requests
import json
import random




# Create your views here.
def index(request):
    return render(request, 'index.html')


def send_mail(request):
    # if request.method == 'POST':
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     recepient = request.POST['email']
    #     print(message)
    send_mail('subject', 'message', 'md.reyajuddin908@gmail.com', ['md.reyajuddin45@gmail.com'], fail_silently=False)
    return render(request, 'send_email.html')


def send_sms(request):
    URL = 'https://www.sms4india.com/api/v1/sendCampaign'

    if request.method == 'POST':
        phone_num = request.POST.get("phoneno")
        msg = request.POST.get("msg")

        req_params = {
            'apikey': 'Y71M36O9JHRH9UHSQHUWTZVLKM9AGVBC',
            'secret': '41VQG66YTEFRBHCH',
            'usetype': 'stage',
            'phone': f'{phone_num}',
            'message': f'{msg}',
            'senderid': 'md.reyajuddin45@gmail.com'
            }
        requests.post(URL, req_params)
        messages.success(request, 'SMS Successfully Sent')

    messages.error(request, 'Sending Error')
    return render(request, 'send_sms.html')


def send_otp(request):
    account_sid = 'AC4b53fec3e605bc7f35aeed880b04ac43'
    auth_token = '06f7fca4d3ff64176163e07243f5127d'
    otp = random.randint(1000, 9999)

    if request.method == 'POST':
        phone_num = request.POST.get("phoneno")

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body='Your otp is-'+ str(otp),
            from_='+15184056257',
            to='+91{}'.format(phone_num))
        print(message.sid)
    return render(request, 'send_otp.html')
