import requests
import json

def send_sms(number, text):
    promt = {
        "number": number,
        "text": text,
        "sign": "SMS Aero",
    }
    url = "https://nikolajgoncarov866@gmail.com:jZV0sQSlLUSaQtd7mQAuKRLvQCy3KLbG@gate.smsaero.ru/v2/sms/send"
    r = requests.post(url, json=promt)

send_sms('89006048008', 'test')