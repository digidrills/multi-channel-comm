from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


GOOD_BOY_URL = (
    "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1"
    "&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
)


@app.route("/", methods=["GET", "POST"])
def reply_any():
    print("reached")
    return str("reply to any") 


@app.route("/wa", methods=["GET", "POST"])
def reply_whatsapp():
    print("RCV MSG CALLBACK")
    print(request.get_data())

    try:
        num_media = int(request.values.get("NumMedia"))
    except (ValueError, TypeError):
        return "Invalid request: invalid or missing NumMedia parameter", 400
    response = MessagingResponse()
    if not num_media:
        msg = response.message("Send us an image!")
    else:
        msg = response.message("Thanks for the image. Here's one for you!")
        msg.media(GOOD_BOY_URL)
    return str(response)


@app.route("/sts", methods=["GET", "POST"])
def status_whatsapp():
    print("STS CALLBACK")
    print(request.get_data())

    response = MessagingResponse()
    msg = response.message("status")
    return str(response)


if __name__ == "__main__":
    #app.run()
    app.run(debug=False, use_reloader=True, host='0.0.0.0', threaded=True)
