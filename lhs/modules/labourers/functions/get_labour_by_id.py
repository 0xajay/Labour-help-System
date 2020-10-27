from lhs.modules.labourers.schemas.labour import Labour
import requests
from datetime import datetime
import base64

def get_access_token(refresh_token):
    try:
        client_id = "22BT9C"
        client_secret = "80f861211a5e1ac9fb79f4e90cd7cf8d"
        secret = client_id+":"+client_secret
        authorization_code = base64.b64encode(secret.encode('ascii'))

        payload = {
            'grant_type':'refresh_token',
            'refresh_token':refresh_token
        }
        header = {"Authorization": "Basic "+authorization_code.decode('ascii')}
        token = requests.post("https://api.fitbit.com/oauth2/token", data=payload, headers=header).json()
        if 'errors' in token:
            raise Exception(token['errors'][0]['errorType'])
        return token
    except Exception as err:
        raise Exception(err)

def get_labour_by_id(labour_id, user_data):
    try:
        labour = Labour.objects(pk=labour_id,visibility=True).first()
        result = labour.to_dict()
        token = get_access_token(result["temp_credentials"]["refresh_token"])
        labour.temp_credentials = token
        header = {"Authorization": "Bearer "+token["access_token"]}
        activity = requests.get('https://api.fitbit.com/1/user/'+result["temp_credentials"]["user_id"]+'/activities/date/'+str(datetime.now().date())+'.json', headers=header).json()
        heart_rate = requests.get('https://api.fitbit.com/1/user/'+result["temp_credentials"]["user_id"]+'/activities/heart/date/'+str(datetime.now().date())+'/1d.json', headers=header).json()
        labour.save()
        return {"statusCode":200, "message":"get labour data successful","data":{'activity':activity,'heart_rate':heart_rate}},200
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500


def get_labour_range_by_id(labour_id,from_date,end_date,user_data):
    try:
        labour = Labour.objects(pk=labour_id,visibility=True).first()
        result = labour.to_dict()
        token = get_access_token(result["temp_credentials"]["refresh_token"])
        labour.temp_credentials = token
        header = {"Authorization": "Bearer "+token["access_token"]}
        activity = requests.get('https://api.fitbit.com/1/user/'+result["temp_credentials"]["user_id"]+'/activities/date/'+from_date+'/'+end_date+'.json', headers=header).json()
        heart_rate = requests.get('https://api.fitbit.com/1/user/'+result["temp_credentials"]["user_id"]+'/activities/heart/date/'+from_date+'/'+end_date+'.json', headers=header).json()
        labour.save()
        return {"statusCode":200, "message":"get labour data successful","data":{'activity':activity,'heart_rate':heart_rate}},200
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
