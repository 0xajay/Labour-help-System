from lhs.modules.users.schemas.user import User
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from lhs.redis.connection import conn
import uuid
from datetime import datetime
from flask import session
from lhs.modules.stripe.hubspoke.create_stripe_customer import create_stripe_customer

def user_register(req):
    firstname = req.get('firstname')
    lastname = req.get('lastname')
    email = req.get('email')
    password = req.get('password')
    try:
        user = User.objects(email=email.lower()).first()
        if user:
            return {"statusCode":406, "message":"email already exist"},406
        else:
            password = generate_password_hash(password)
            stripe_customer,stripe_client_secret = create_stripe_customer(email)
            new_user = User(firstname=firstname,lastname=lastname,email=email.lower(),password=password, permission="USER",stripe_customer_id=stripe_customer,stripe_client_secret=stripe_client_secret).save()
            result = new_user.to_dict()
            id = str(uuid.uuid1())
            session["id"] = id
            info = {"sessionId": session["id"], "valid": "True","userid": result["id"], "timestamp":str(datetime.now())}
            conn.hmset(session["id"], info)
            access_token = create_access_token(identity=id)
            return {"statusCode":201,"message":"user registration successful","data":{**result, 'jwt':access_token,}},201


    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
