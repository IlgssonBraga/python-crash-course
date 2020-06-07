# Create List

numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor

numbers2 = list((1, 2, 3, 4, 5))

print(numbers)
print(numbers2)

# Get a value

print(fruits[1])

# Get length

print(len(fruits))

# Change value

fruits[1] = 'Strawberries'

# Append do list

fruits.append('Mangos')

print(fruits)

# Remove from list

fruits.remove('Grapes')

print(fruits)

# Insert into position 

fruits.insert(3, 'Grapes')

print(fruits)

# Remove with pop

fruits.pop(1)

print(fruits)

# Reverse list

fruits.reverse()

print(fruits)

# Sort list

fruits.sort()

print(fruits)

# Reverse sort

fruits.sort(reverse=True)

print(fruits)