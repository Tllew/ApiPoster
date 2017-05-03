from Settings import jsonString
from Settings import uniqueKey
from Settings import uniqueValue

def createJson(data):
    result = jsonString
    if uniqueKey:
        result = {data[uniqueValue] : jsonString}
    for key in data:
        populateLowLevel(jsonString,key,data[key])
    return result

def populateLowLevel(jsonString,key,value):
    for x in jsonString:
        if key == x:
            jsonString[x] = value
            return jsonString;
        if type(jsonString[x]) == dict:
            branch = populateLowLevel(jsonString[x], key, value)
            if branch:
                return branch