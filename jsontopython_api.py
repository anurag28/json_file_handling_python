import json
from urllib.request import urlopen

with urlopen("https://jsonplaceholder.typicode.com/todos/1/users") as response:
    source = response.read()


data = json.loads(source)

#print(json.dumps(data, indent=2))

print(len(data))

users = dict()

for d in data:
    users[d['id']] = d['address']

print(users.keys())
print(users.values())


