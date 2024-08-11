# access unique val in json
import json
python_obj = '{"Size":  "M", "Size":  "XL", "Size":  "XXL", "Size": "S", "Waist": 25, "Waist": 28}'
json_obj = json.loads(python_obj)
print(json_obj)
