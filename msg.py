from __future__ import print_function
import time
import Telstra_Messaging
import sys
from Telstra_Messaging.rest import ApiException
from pprint import pprint
import json

PROVISION_NUMBER = '+61472880727'

def send_texts(message, numbers):

	# message: str
	# name: str
	# numbers: [str]

	# Generating the access token to use the Telstra Messaging API 
	token = generate_token()

	if not token:
		sys.stderr.write("Exception when calling AuthenticationApi->auth_token: %s\n" % ApiException)
		sys.exit(1)

	# Configure OAuth2 access token for authorization: auth
	configuration = Telstra_Messaging.Configuration()
	configuration.access_token = token

	# create an instance of the API class
	api_instance = Telstra_Messaging.MessagingApi(Telstra_Messaging.ApiClient(configuration)) 

	# Configure the message that will be sent out to people
	# message = "Hi {}, we are contacting you from Hedwig HQ to let you know that {}, Have a good day. Stay Safe.".format(name, message)

	# Send an sms to all the chosen numbers 
	for idx in range(len(numbers)):

		send_sms_request = Telstra_Messaging.SendSMSRequest(numbers[idx], message, PROVISION_NUMBER)
		 # SendSMSRequest | A JSON or XML payload containing the recipient's phone number and text message.
		# This number can be in international format if preceeded by a '+' or in national format ('04xxxxxxxx') where x is a digit.

		try:
		    # Send SMS
		    api_response = api_instance.send_sms(send_sms_request)
		    pprint(api_response)
		except ApiException as e:
		    print("Exception when calling MessagingApi->send_sms: %s\n" % e)

def generate_token():

	api_instance = Telstra_Messaging.AuthenticationApi()
	client_id = 'W7XTGuE7Oozy3ID8c9gbUgTh4AlZEDxF' # str | 
	client_secret = '0ZnGtffkmF1ImKAp' # str | 
	grant_type = 'client_credentials' # str |  (default to 'client_credentials')

	try:
    # Generate OAuth2 token
	    api_response = api_instance.auth_token(client_id, client_secret, grant_type)

	    return api_response.access_token

	except ApiException as e:
		return None
	    

if __name__ == "__main__":
	# if len(sys.argv) != 4:
	# 	sys.stderr.write("Incorrect number of arguments")
	# 	sys.exit(1)

	# # This call method is only for testing purposes when testing on a single phone 
	# massText(sys.argv[1], sys.argv[2], [sys.argv[3]])
	# print(generate_token()) 
	numbers = ["+610411092996"]
	message = "todo test"
	send_texts(message, numbers)