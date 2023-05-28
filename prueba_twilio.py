# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACbaedc2db785c81503d2e0841e9101bf6']
auth_token = os.environ['f26edffa50209bb82baf63f71209e0ff']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='+13157079249',
                              media_url=['https://demo.twilio.com/owl.png'],
                              to='+528125786597'
                          )

print(message.sid)
