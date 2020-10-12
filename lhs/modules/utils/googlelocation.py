import requests
from resonance import app
import os

url = "https://maps.googleapis.com/maps/api/geocode/json"
timezone_url = "https://maps.googleapis.com/maps/api/timezone/json"

api_key = os.environ.get('GOOGLE_TIMEZONE_API')

def get_location(lat,long):
    params = {'sensor': 'false', 'latlng':str(lat)+","+str(long), 'key':api_key}
    result = requests.get(url, params=params)
    return result

def get_locationbyplaceid(placeid):
    params = {'sensor': 'false', 'place_id':str(placeid), 'key':api_key}
    result = requests.get(url, params=params)
    return result

def get_locationtimezone(lat,long):
    params = {'location':str(lat)+","+str(long),'timestamp':'1458000000','key':api_key}
    result = requests.get(timezone_url,params=params)
    return result.json()
