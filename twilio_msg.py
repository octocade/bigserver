# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


with open('tokens', 'r') as fh:
	tokens = eval(fh.read())

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = tokens["account_sid"] #os.environ['TWILIO_ACCOUNT_SID']
auth_token = tokens["auth_token"] #os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="fJoin Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15033038791',
                     to='+61411092996'
                 )

print(message.sid)