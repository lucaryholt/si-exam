import os

import os

token_database = {}


def get_api_key():
    return os.environ['FAT_SMS_API_KEY']


def get_email():
    return os.environ['DEFAULT_USER_EMAIL']


def get_name():
    return os.environ['DEFAULT_USER_NAME']


def get_last_name():
    return os.environ['DEFAULT_USER_LAST_NAME']


def get_phone():
    return os.environ['DEFAULT_USER_PHONE']
