from mongoengine import *
from datetime import datetime


class Card(Document):
    user_id = StringField(required=True)
    name = StringField(required=True)
    card_number = StringField(required=False)
    expiry_date = StringField(required=False)
    cvv = StringField(required=True)
    visibility = BooleanField(required=True, default=True)
    timestamp = DateTimeField(default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.pk),
            "user_id":self.user_id,
            "name":self.name,
            "card_number":self.card_number,
            "expiry_date":self.expiry_date,
            "cvv":self.cvv,
            "visibility":self.visibility,
            "timestamp":str(self.timestamp)
        }
