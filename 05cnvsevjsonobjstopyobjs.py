import json
json_obj_1 = '{"Name": "Daniel", "Age": "45", "Education": "BS"}'
json_obj_2 = '["Red", "Green", "Black"]'
json_obj_3 = '"Python Json"'
json_obj_4 = '1234'
json_obj_5 = '12.43'
py_obj_1 = json.loads(json_obj_1)
print(py_obj_1)
py_obj_2 = json.loads(json_obj_2)
print(py_obj_2)
py_obj_3 = json.loads(json_obj_3)
print(py_obj_3)
py_obj_4 = json.loads(json_obj_4)
print(py_obj_4)
py_obj_5 = json.loads(json_obj_5)
print(py_obj_5)
