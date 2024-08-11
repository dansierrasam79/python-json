# convert multiple py objects to JSON strs
import json
py_dict = {1:{"name": "David", "age": 6, "class":"I"}, 2:["Red", "Green", "Black"], 3: "Python JSON", 4: 1234, 5:21.35, 5: True, 6:False, 7:None}
json_1 = json.dumps(py_dict[1])
json_2 = json.dumps(py_dict[2])
json_3 = json.dumps(py_dict[3])
json_4 = json.dumps(py_dict[4])
json_5 = json.dumps(py_dict[5])
json_6 = json.dumps(py_dict[6])
json_7 = json.dumps(py_dict[7])
print(json_1)
print(json_2)
print(json_3)
print(json_4)
print(json_5)
print(json_6)
print(json_7)
