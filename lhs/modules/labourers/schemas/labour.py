from mongoengine import *
from datetime import datetime


class Labour(Document):
    name = StringField(required=True)
    designation = StringField(required=True)
    phone = StringField(required=True)
    country_code = StringField(required=True)
    email = StringField(required=True)
    temp_credentials = DictField(required=True)
    visibility = BooleanField(required=True, default=True)
    timestamp = DateTimeField(default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.pk),
            "name":self.name,
            "designation":self.designation,
            "phone":self.phone,
            "country_code":self.country_code,
            "temp_credentials":self.temp_credentials,
            "visibility":self.visibility,
            "timestamp":str(self.timestamp)
        }
