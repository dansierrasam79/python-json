#convert sorted py object to JSON with indent level 4
import json
JSON_obj = {'14': 5, '26': 7, '8': 3, '2': 4}
print(json.dumps(JSON_obj,sort_keys=True,indent=4))
