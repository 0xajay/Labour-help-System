from lhs.modules.labourers.schemas.labour import Labour


def get_labourers(user_data):
    try:
        labourers = Labour.objects(visibility=True)
        result = [labour.to_dict() for labour in labourers]
        return {"statusCode":200, "message":"get labourers successful","data":result},200
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500    
