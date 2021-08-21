from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = Telstra_Messaging.Configuration()
configuration.access_token = 'AgMJq616NePrIonLAgJq6PFNGBUj'

# create an instance of the API class
api_instance = Telstra_Messaging.ProvisioningApi(Telstra_Messaging.ApiClient(configuration))
provision_number_request = Telstra_Messaging.ProvisionNumberRequest(10) # ProvisionNumberRequest | A JSON payload containing the required attributes

try:
    # Create Subscription
    api_response = api_instance.create_subscription(provision_number_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningApi->create_subscription: %s\n" % e)

    # New num: {'destination_address': '+61472880727', 'expiry_date': 1632170558599.0}
