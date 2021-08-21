# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC1f0869b647a49e8153bc2b3133049a92" #os.environ['TWILIO_ACCOUNT_SID']
auth_token = "36ec5157daef9ea4b15bc79a0c3cd77c" #os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15033038791',
                     to='+61411092996'
                 )

print(message.sid)