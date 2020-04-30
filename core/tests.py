# from twilio.rest import Client
#
# account_sid = 'AC4b53fec3e605bc7f35aeed880b04ac43'
# auth_token = '06f7fca4d3ff64176163e07243f5127d'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#          body='This is the ship that made the Kessel Run in fourteen parsecs?',
#          from_='+15017122661',
#          to='9583285786'
#      )
#
# print(message.sid)

from django.core.mail import send_mail
from django.conf import settings

send_mail('subject', 'message', 'md.reyajuddin908@gmail.com', ['md.reyajuddin45@gmail.com'], fail_silently=False)


#
# def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
#   req_params = {
#   'apikey':apiKey,
#   'secret':secretKey,
#   'usetype':useType,
#   'phone': phoneNo,
#   'message':textMessage,
#   'senderid':senderId
#   }
#   return requests.post(reqUrl, req_params)
#
# # get response
# response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
# """
#   Note:-
#     you must provide apikey, secretkey, usetype, mobile, senderid and message values
#     and then requst to api
# """
# # print response if you want
# print response.text
