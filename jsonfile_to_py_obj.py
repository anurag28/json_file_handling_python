import json

with open('sample.json') as f:
    data = json.load(f)

for markers in data["markers"]:
    print(markers['name'], markers['location'])
    del markers['id']

with open("sample2.json", "w") as f:
    json.dump(data, f, indent=2)