from lhs.modules.users.schemas.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from lhs.redis.connection import conn
import uuid
from datetime import datetime
from flask import session


def get_login(req):
    email = req.get("email").lower()
    password = req.get('password')
    try:
        user = User.objects.get(email=email)
        if user:
            if check_password_hash(user.password,password):
                user = user.to_dict()
                id = str(uuid.uuid1())
                session["id"] = id
                info = {"sessionId": session["id"], "valid":"True","userid":user["id"],"timestamp":str(datetime.now())}
                conn.hmset(session["id"],info)
                access_token = create_access_token(identity=id)
                return {"statusCode":200,"message":"login successful","data":{**user, "jwt":access_token}},200
            else:
                return {"statusCode":401,"message":"invalid credentials"},401
        else:
            return {"statusCode":401,"message":"invalid credentials"},401
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
