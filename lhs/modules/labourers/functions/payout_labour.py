from lhs.modules.labourers.schemas.transaction import Transaction
from lhs.modules.labourers.schemas.labour import Labour

def payout_labour(req,user_data):
    amount = req.get('amount')
    card_id = req.get('card_id')
    labour_id = req.get('labour_id')
    try:
        receiver = Labour.objects(pk=labour_id,visibility=True).first()
        receiver = receiver.to_dict()
        receiver_name = receiver["name"]
        transaction = Transaction(sender_id=str(user_data.id), receiver_id=labour_id, sender_name=user_data.firstname+" "+user_data.lastname, receiver_name= receiver_name, amount=amount).save()
        transaction = transaction.to_dict()
        # result = [transaction.to_dict() for transaction in transactions]
        return {"statusCode":200, "message":"post transaction successful","data":transaction},200
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
