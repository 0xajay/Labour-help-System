from lhs.modules.payments.schemas.card import Card

def add_new_card(req, user_data):
    name = req.get('name')
    card_number = req.get('card_number')
    expiry_date = req.get('expiry_date')
    cvv = req.get('cvv')
    try:
        new_card = Card(name=name, card_number=card_number, expiry_date=expiry_date, cvv=cvv, user_id=str(user_data.id)).save()
        result = new_card.to_dict()
        return {"statusCode":201, "message":"card added successful","data":result},201
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
