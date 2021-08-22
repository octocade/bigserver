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
	0: "hello izzie, keep messaging me",
	1: "or should i call you?...",
	2: "isadora",
	3: "good morning",
	4: "wake me up inside"
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
    print("Person sent us: " + body)

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