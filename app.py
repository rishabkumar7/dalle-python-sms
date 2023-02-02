from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def dalle2():
  """get incoming message"""
  inb_msg = request.form['Body'].lower()
  print(inb_msg)
  response = openai.Image.create(
    prompt=inb_msg,
    n=1,
    size="1024x1024"
  )
  """Respond to incoming calls with a simple text message."""
  # Start our TwiML response
  resp = MessagingResponse()
  msg = resp.message()
  # Add a media response
  imgUrl = response['data'][0]['url']
  print(response['data'][0]['url'])
  msg.media(imgUrl)

  return str(resp)

if __name__ == "__main__":
    app.run(debug=True)