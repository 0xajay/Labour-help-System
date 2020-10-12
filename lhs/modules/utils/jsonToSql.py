import json
from resonance import db

def JsonToSqlUpdate(dbname,data):
    try:
        for key in data:
            if len(str(data[key]))>0:
                setattr(dbname, key, data[key])
        db.session.commit()
        return True

    except Exception as e:
        db.session.rollback()
        raise Exception(e)
