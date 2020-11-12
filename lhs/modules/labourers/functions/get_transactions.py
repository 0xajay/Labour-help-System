from lhs.modules.labourers.schemas.transaction import Transaction
from mongoengine.queryset.visitor import Q
from datetime import datetime

def get_transactions(start_date,end_date, user_data):
    try:
        kwargs = {}
        start = datetime.strptime(start_date,'%Y-%M-%d')
        end =  datetime.strptime(end_date,'%Y-%M-%d')
        reports = Transaction.objects()
        result = [report.to_dict() for report in reports]
        return {"statusCode":200, "message":"get transactions","data":result},200
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
