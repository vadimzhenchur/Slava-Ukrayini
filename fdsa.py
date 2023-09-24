import json

with open("data.json", 'r') as f:
    data = json.load(f)

data['age'] = 14
data['name'] = 'Vadym Zhenchur'
data['occupation'] = 'CORD'
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

