#create new json file using old file
import json
with open('marks.json') as f:
  stud_data= json.load(f)

with open('new_marks.json', 'w') as f:
  json.dump(stud_data, f, indent=2)
