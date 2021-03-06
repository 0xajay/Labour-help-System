from mongoengine import *
from datetime import datetime


class Labour(Document):
    name = StringField(required=True)
    designation = StringField(required=True)
    phone = StringField(required=True)
    country_code = StringField(required=True)
    email = StringField(required=True)
    amount = IntField(required=False, default=0)
    temp_credentials = DictField(required=True)
    visibility = BooleanField(required=True, default=True)
    timestamp = DateTimeField(default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.pk),
            "name":self.name,
            "designation":self.designation,
            "email":self.email,
            "phone":self.phone,
            "country_code":self.country_code,
            "amount":self.amount,
            "temp_credentials":self.temp_credentials,
            "visibility":self.visibility,
            "timestamp":str(self.timestamp)
        }
