import os
import requests
from services.database import get_api_key, get_phone


def send_token(token):
    message = f"Token {token}"

    print(f"DEBUG - Token: {token}")

    payload = {'to_phone': get_phone(), 'message': message,
               'api_key': get_api_key()}

    api_endpoint = os.environ['FAT_SMS_ENDPOINT']

    r = requests.post(f'{api_endpoint}/send-sms',
                      data=payload)

    print('DEBUG - SMS Response:', r.text)

    return get_phone()
