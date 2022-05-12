import os

import os
import mysql.connector
from mysql.connector import Error

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


def save_token(email, phone, token):
    try:
        connection = mysql.connector.connect(
            host="192.168.1.152", database="nietzsche", user="tirionadmin", password="xiGTNicJvX4Pdn")

        if connection.is_connected():
            cursor = connection.cursor()
            result = cursor.execute(
                f"INSERT INTO token (email, phone, token) VALUES ('{email}', {phone}, '{token}');")

            connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
