import json

people_string = '''
{
    "people": [
        {
            "name": "John Doe",
            "phone": "226-929-6586",
            "emails": ["john@gmail.com", "doe@hotmail.com"],
            "has_licence": false
        },
        {
            "name": "Jim Carry",
            "phone": "226-929-6588",
            "emails": null,
            "has_licence": true
        }
    ]
}
'''

data = json.loads(people_string)
print(data)
print(type(data['people']))

for person in data['people']:
    print(person['name'])
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)