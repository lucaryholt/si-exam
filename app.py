from bottle import default_app, get, run, view, request, post
from dotenv import load_dotenv
from services.jwt_services import get_secret_key
from services.sms_service import send_token as send_sms_token
from services.email_service import send_token as send_email_token
from services.database import get_email, get_phone, token_database, save_token
import os
import jwt
import random
import time
import uuid

load_dotenv()


@get("/")
@view("index")
def _():
    return


@get("/welcome")
@view("welcome")
def _():
    return


@post("/verify")
def _():
    jwt_token = request.json.get("jwt")

    print(jwt_token, get_secret_key())

    try:
        jwt_decoded = jwt.decode(
            jwt_token, get_secret_key(), algorithms=["HS256"])

        if int(jwt_decoded['exp']) > int(time.time()):
            random_token = random.randint(1000, 9999)

            phone = send_sms_token(random_token)
            send_email_token(get_email(), random_token)

            token_database[phone] = random_token

            return {"status": 'YES'}
        else:
            return {"status": 'NO'}
    except jwt.exceptions.DecodeError:
        return {"status": "ERROR"}


@post("/validate-token")
def _():
    token = int(request.json.get("token"))

    try:
        database_entry = token_database[get_phone()]

        if not database_entry:
            return {"status": "NO"}

        if database_entry == token:
            esb_token = uuid.uuid4()
            save_token(get_email(), get_phone(), esb_token)
            return {"status": "YES", "token": str(esb_token)}

        return {"status": "NO"}
    except KeyError:
        return {"status": "NO"}


try:
    # Server AWS (Production)
    import production
    application = default_app()
except:
    host = os.environ['HOST']
    port = os.environ['PORT']

    # Local machine (Development)
    run(host=host, port=port,
        debug=True, reloader=True, server="paste")
