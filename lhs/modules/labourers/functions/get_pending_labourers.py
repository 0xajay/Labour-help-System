from lhs.modules.labourers.schemas.labour import Labour

def get_pending_labourers(user_data):
    try:
        labourers = Labour.objects(device_added=False)
        result = [ labour.to_dict() for labour in labourers]
        return {"statusCode":200, "message":"get pending labourers successful","data":result},200
    except Exception as err:
        {"statusCode":500, "message":str(err)},500
