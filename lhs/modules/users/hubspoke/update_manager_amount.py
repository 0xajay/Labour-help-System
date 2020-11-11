from lhs.modules.users.schemas.user import User


def update_manager_amount(amount, id):
    try:
        manager = User.objects(pk=str(id)).first()
        old_amount = manager.amount
        manager.amount = old_amount + amount
        manager.save()
    except Exception as err:
        raise Exception(err)
