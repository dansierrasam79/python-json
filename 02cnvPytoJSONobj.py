# convert python object to JSON object
import json
py_object = {'Name': 'Daniel', 'Age': '45', 'Education': 'BS'}
json_obj = json.dumps(py_object)
print(type(json_obj))
print(json_obj)
