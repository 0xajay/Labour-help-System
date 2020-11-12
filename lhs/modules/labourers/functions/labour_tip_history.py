from lhs.modules.labourers.schemas.transaction import Transaction


def labour_tip_history(labour_id,user_data):
    try:
        transactions = Transaction.objects(sender_id=str(user_data.id), receiver_id=labour_id)
        result = [transaction.to_dict() for transaction in transactions]
        return {"statusCode":200, "message":"get transactions successful","data":result},200
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
