
def sqlToJson(sqlresults,fields):
    result = []
    for sqlresult in sqlresults:
        sql_row = {}
        for field in fields:
            sql_row[field] = sqlresult[field]
        result.append(sql_row)
    return result

def contract_sqlToJson(sqlresults,fields):
    result = []
    for sqlresult in sqlresults:
        sql_row = {}
        for field in fields:
            sql_row[field] = str(sqlresult[field])
        result.append(sql_row)
    return result
