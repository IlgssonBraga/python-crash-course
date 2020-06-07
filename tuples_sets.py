# Create tuple

fruits = ('Apples', 'Oranges', 'Grapes')

# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

fruits2 = ('Apples')

# Single values needs trailing comma
fruits3 = ('Apples',)

print(fruits)
print(type(fruits2))
print(type(fruits3))

# Get value

print(fruits[1])

# Can't change a value

# fruits[0] = 'Pears'

# Size

print(len(fruits))

# Delete

del fruits2

# print(fruits2)

# SETS

# Create a set

fruits_set = {'Apples', 'Oranges', 'Grapes'}

print(fruits_set)

# Check if in set

print('Bananas' in fruits_set)

# Add to set

fruits_set.add('Pears')

print(fruits_set)

# Remove from set

fruits_set.remove('Pears')

print(fruits_set)

# Clear set

fruits_set.clear()

print(fruits_set)

# Delete all set

del fruits_set

# print(fruits_set)