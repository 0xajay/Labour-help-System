from lhs.modules.labourers.schemas.labour import Labour
import requests
import base64


def get_access_token(code):
    client_id = "22BT9C"
    client_secret = "80f861211a5e1ac9fb79f4e90cd7cf8d"
    secret = client_id+":"+client_secret
    authorization_code = base64.b64encode(secret.encode('ascii'))

    url = "https://api.fitbit.com/oauth2/token"
    header = {"Authorization": "Basic "+authorization_code.decode('ascii')}
    payload = {
        'grant_type':'authorization_code',
        'code':code,
        'client_id':client_id,
        'redirect_uri':'http://localhost:3000/authenticate_device'
    }

    token = requests.post(url, data=payload, headers=header).json()
    return token


def create_labour(req, user_data):
    name = req.get('name')
    designation = req.get('designation')
    phone = req.get('phone')
    country_code = req.get('country_code')
    email = req.get('email')
    try:
        tokens = get_access_token(req.get('code'))
        labour = Labour(name=name,designation=designation,email=email, phone=phone, country_code=country_code, temp_credentials=tokens).save()
        result = labour.to_dict()
        return {"statusCode":201, "message":"Labour creation successful","data":result},201
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
