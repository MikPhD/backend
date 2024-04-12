import os
import json
import re
from flask import Flask, render_template, request, session, Response, redirect, send_file, jsonify
import aiohttp

###################### Start the FLASK app
app = Flask(__name__)

@app.route("/webapp")
def home():
    return 'ciao hello world'

@app.get("/whatsapp")
async def send_message(data):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {'blue_panda'}",
    }

    async with aiohttp.ClientSession() as session:
        url = 'https://graph.facebook.com' + f"/'v18.0/297954746725420/messages"
        try:
            async with session.post(url, data=data, headers=headers) as response:
                if response.status == 200:
                    print("Status:", response.status)
                    print("Content-type:", response.headers['content-type'])

                    html = await response.text()
                    print("Body:", html)
                else:
                    print(response.status)
                    print(response)
        except aiohttp.ClientConnectorError as e:
            print('Connection Error', str(e))


def get_text_message_input(recipient, text):
    return json.dumps({
        "messaging_product": "whatsapp",
        "preview_url": False,
        "recipient_type": "individual",
        "to": recipient,
        "type": "text",
        "text": {
            "body": text
        }
    })
