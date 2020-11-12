from mongoengine import *
from datetime import datetime


class Transaction(Document):
    sender_id = StringField(required=True)
    receiver_id = StringField(required=True)
    sender_name = StringField(required=False)
    receiver_name = StringField(required=False)
    amount = IntField(required=True)
    payment_status = BooleanField(required=True, default=False)
    visibility = BooleanField(required=True, default=True)
    timestamp = DateTimeField(default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.pk),
            "sender_id":self.sender_id,
            "receiver_id":self.receiver_id,
            "sender_name":self.sender_name,
            "receiver_name":self.receiver_name,
            "amount":self.amount,
            "payment_status":self.payment_status,
            "visibility":self.visibility,
            "timestamp":str(self.timestamp)
        }
