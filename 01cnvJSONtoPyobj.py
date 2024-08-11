# convert JSON to Py object
import json
json_object = '{"Name":"Daniel", "Age": "45", "Education": "BS"}'
py_object = json.loads(json_object)
print(py_object)
print(py_object["Name"])
print(py_object["Age"])
print(py_object["Education"])
