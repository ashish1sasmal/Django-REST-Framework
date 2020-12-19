import json
from .models import Employee

def is_json(data):
    try :
        dict_data = json.loads(data)
        return True
    except:
        return False

def get_object_by_id(id):
    try:
        emp = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        emp=None
    return emp
