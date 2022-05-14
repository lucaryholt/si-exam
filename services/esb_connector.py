from urllib import request


import requests
import os


def send_esb_token(email, phone, token):
    esb_endpoint = os.environ['ESB_ENDPOINT']
    esb_admin_key = os.environ['ESB_ADMIN_KEY']

    payload = {'email': email, 'phone': int(phone), 'token': str(token)}

    headers = {'X-Api-Key': esb_admin_key, 'Content-Type': 'application/json'}

    r = requests.post(f'{esb_endpoint}/token', headers=headers, json=payload)

    print('DEBUG - ESB Token Response:', r.text)

    return r.status_code == 200
