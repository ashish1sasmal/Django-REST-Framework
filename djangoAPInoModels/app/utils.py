import json

def is_json(data):
    try :
        dict_data = json.loads(data)
        return True
    except:
        return False
