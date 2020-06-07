# Create dict

person = {
    'first_name': 'Ilgsson',
    'last_name': 'Braga',
    'age': 25
}

# Use constructor

# person2 = dict(first_name='Ilgsson',last_name='Braga',age=25)

print(person, type(person))

# print(person2, type(person2))

# Get a single value

print(person['first_name'])
print(person.get('last_name'))

# Add key/value

person['phone'] = '81997562577'

print(person)

# Get dict keys

print(person.keys())

# Get dict items

print(person.items())

# Copy dict

person2 = person.copy()

person2['City'] = 'Nazaré da Mata'

print(person2)

# Remove item

del person['age']
person.pop('phone')

print(person)

# Clear

person.clear()

print(person)

# Get length

print(len(person2))

# List of dict

people = [
    {'name': 'Ilgsson', 'age': 25},
    {'name': 'Arlaine', 'age': 24}
]

print(people[0]['name'])