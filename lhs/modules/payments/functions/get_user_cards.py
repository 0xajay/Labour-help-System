from lhs.modules.payments.schemas.card import Card

def get_user_cards(user_data):
    try:
        print(user_data.id)
        cards = Card.objects(user_id=str(user_data.id))
        result = []
        for card in cards:
            card = card.to_dict()
            card_number = card["card_number"][0:3]+'X'*9+card["card_number"][-4:]
            card["card_number"] = card_number
            result.append(card)
        return {"statusCode":200, "message":"get cards successful","data":result},200
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
