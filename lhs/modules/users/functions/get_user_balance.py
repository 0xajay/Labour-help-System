from lhs.modules.users.schemas.user import User

def get_user_balance(user_data):
    try:
        user = User.objects(pk=str(user_data.id)).first()
        print(user.amount)
        return {"statusCode":200, "message":"get user balance successful","data":user.amount},200
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
