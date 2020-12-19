import json
from .models import Student

def is_json(data):
    try :
        dict_data = json.loads(data)
        return True
    except:
        return False

def get_object_by_id(id):
    try:
        emp = Student.objects.get(id=id)
    except Student.DoesNotExist:
        emp=None
    return emp
