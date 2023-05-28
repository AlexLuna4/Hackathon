# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACbaedc2db785c81503d2e0841e9101bf6"
auth_token = "f26edffa50209bb82baf63f71209e0ff"
client = Client(account_sid, auth_token)

message = client.messages.create(                          
                             to="+528125786597",
                             from_="+13157079249",
                             body="Hello from Python!"
                          )

print(message.sid)
