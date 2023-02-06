from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from queryHandler import QueryResponse
app = Flask(__name__)

@app.route("/")
def Home():
    return "Hello world"

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    # Add a message
    body = request.values.get('Body', None)
    resp.message(QueryResponse(body))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)