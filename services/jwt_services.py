import os


def get_secret_key():
    return os.environ['JWT_SECRET_KEY']
