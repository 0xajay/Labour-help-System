from mongoengine import *
from datetime import datetime


class User(Document):
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    phone = StringField(required=False)
    country_code = StringField(required=False)
    email = EmailField(required=True)
    password = StringField(required=True)
    profile_pic = StringField(required=False)
    permission = StringField(required=True)
    visibility = BooleanField(required=True, default=True)
    timestamp = DateTimeField(default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.pk),
            "firstname":self.firstname,
            "lastname":self.lastname,
            "phone":self.phone,
            "country_code":self.country_code,
            "email":self.email,
            "profile_pic":self.profile_pic,
            "permission":self.permission,
            "visibility":self.visibility,
            "timestamp":str(self.timestamp)
        }
