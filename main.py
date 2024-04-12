from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Le origini consentite
    allow_credentials=True,
    allow_methods=["*"],  # Permette tutti i metodi
    allow_headers=["*"],  # Permette tutti gli header
)


@app.get("/get")
async def root(id: str = Query(None)):
    return 'hello world'
    # response = {
    #     "message": "Hello World",
    #     "client_id": id  # Includi l'ID nella risposta per confermare che è stato ricevuto
    # }
    # print(response)
    #
    # return json.dumps((f"Rispondo per conto di: {id}", 'Risposta'))
    # return json.dumps((f"Rispondo per conto di: ", 'Risposta'))


# @app.get("/get")
# async def send_message(data):
#     headers = {
#         "Content-type": "application/json",
#         "Authorization": f"Bearer {current_app.config['ACCESS_TOKEN']}",
#     }
#
#     async with aiohttp.ClientSession() as session:
#         url = 'https://graph.facebook.com' + f"/{current_app.config['VERSION']}/{current_app.config['PHONE_NUMBER_ID']}/messages"
#         try:
#             async with session.post(url, data=data, headers=headers) as response:
#                 if response.status == 200:
#                     print("Status:", response.status)
#                     print("Content-type:", response.headers['content-type'])
#
#                     html = await response.text()
#                     print("Body:", html)
#                 else:
#                     print(response.status)
#                     print(response)
#         except aiohttp.ClientConnectorError as e:
#             print('Connection Error', str(e))
#
#
# def get_text_message_input(recipient, text):
#     return json.dumps({
#         "messaging_product": "whatsapp",
#         "preview_url": False,
#         "recipient_type": "individual",
#         "to": recipient,
#         "type": "text",
#         "text": {
#             "body": text
#         }
#     })