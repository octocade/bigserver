from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
	return "hello world <3"

counter = 0

@app.route('/reset')
def reset():
	counter = 0
	return "counter is: " + str(counter)

@app.route('/counter')
def counter():
	return "counter is: " + str(counter)

RESP = {
	0: "hello izzie",
	1: "or should i call you?...",
	2: "isadora",
	3: "good morning",
	4: "wake me up inside"
}
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    if counter in RESP:
    	msg = RESP[counter]
    else:
    	msg = "good luck buddy!"
    # Add a message
    resp.message(msg)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)