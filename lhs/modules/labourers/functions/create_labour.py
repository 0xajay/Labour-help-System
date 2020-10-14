from lhs.modules.labourers.schemas.labour import Labour


def create_labour(req, user_data):
    name = req.get('name')
    designation = req.get('designation')
    phone = req.get('phone')
    country_code = req.get('country_code')
    try:
        labour = Labour(name=name,designation=designation, phone=phone, country_code=country_code).save()
        result = labour.to_dict()
        return {"statusCode":201, "message":"Labour creation successful","data":result},201
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
