import json
import requests

'''
message = {
    "event": "send",
    "user" : user,
    "textContent": {
        "text": sendMSG
    }
}
'''

def sender(message):
    param = {'event':'send', 'user':'test', 'textContent':{'text':message}}
    url = 'http://localhost:8000/download'
    header={'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(url=url, headers=header, data=json.dumps(param))
    return response

def reciever(response):
    data = response.json()
    message = data['textContent']['text']
    print("Server << " + message)
    return message

while True:
    message = input("User >> ")
    response = sender(message)
    reciever(response)
