from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

global counter
counter = 0

@app.route("/")
def hello():
	return "hello world <3"


@app.route('/reset')
def reset():
	counter = 0
	return "counter is: " + str(counter)

@app.route('/counter')
def get_counter():
	print("counter is: " + str(counter))
	return "counter is: " + str(counter)

RESP = {
	0: "Good morning Tim! 🌅",
	1: "Just checking in, how is your day going Tim?",
	2: "Great to hear 😊 Keep powering through!",
	3: "Just checking in, how is your evening going Tim? 🌇",
	4: "Would you us to put you through to a counsellor?",
	5: "Would you to chat with a friend?",
	6: "You haven't talked to your buddy in a while! They are active https://www.messenger.com/t/1302711535",
	7: "Good night Tim! 😴"
}

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response   
    global counter
    resp = MessagingResponse()
    print("counter is: " +  str(counter))

    # TODO: remove state, used script.
     # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print("Person sent us: " + str(body))

    if counter in RESP:
    	msg = RESP[counter]
    	counter += 1
    else:
    	msg = "bye for now 😋"
    	# Resets.
    	counter = 0
    # Add a message
    resp.message(msg)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)