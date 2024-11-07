import json

def to_json(data):
    return json.dumps(data).replace('True', 'true').replace('False', 'false')