name = 'Ilgsson'
age = 25

# Concatnate

print('Hello, my name is ' + name + 'and I am ' + str(age))

# String Formatting

# Arguments by position

print("My name is {name} and I am {age}".format(name=name, age=age))

# F-strings

print(f'Hello, my name is {name} and I am {age}')

# String methods

s = 'hello world'

# Capitalize

print(s.capitalize())

# Upper

print(s.upper())

# Lower

print(s.lower())

# Swap case

print(s.swapcase())

# Length

print(len(s))

# Replace

print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with

print(s.startswith('hello'))

# End with

print(s.endswith('world'))

# Split into a list

print(s.split())

# Find position

print(s.find('r'))

# Is all alphanumeric

print(s.isalnum())

# Is all alphabetic

print(s.isalpha())

# Is all numeric

print(s.isnumeric())