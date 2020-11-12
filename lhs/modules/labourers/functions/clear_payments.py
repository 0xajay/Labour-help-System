from lhs.modules.labourers.schemas.transaction import Transaction
from lhs.modules.labourers.schemas.labour import Labour
from lhs.modules.users.hubspoke.update_manager_amount import update_manager_amount

def update_labour_amount(amount, id):
    try:
        labour = Labour.objects(pk=str(id)).first()
        old_amount = labour.amount
        labour.amount = old_amount + amount
        labour.save()
    except Exception as err:
        raise Exception(err)

def clear_payments(user_data):
    try:
        transactions = Transaction.objects(payment_status=False)
        for transaction in transactions:
            amount = transaction.amount
            manager_amount = 5*int(amount) / 100
            labour_amount = amount - manager_amount
            update_labour_amount(labour_amount, transaction.receiver_id)
            update_manager_amount(manager_amount, user_data.id)
            transaction.payment_status = True
            transaction.save()

        return {"statusCode":201, "message":"transactions successful"},201
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
