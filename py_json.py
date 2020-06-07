import json

# Sample JSON

userJSON = '{"first_name": "Ilgsson", "last_name":"Braga", "age": 25}'

# Parse to dict

user = json.loads(userJSON)

print(user)

# Parse to JSON

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)