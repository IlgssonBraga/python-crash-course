# if/elif/else

x = 11
y = 10

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# Nested if

if x > 2:
    if x <= 10:
       print(f'{x} is greater than 2 and less than 10') 

if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than 10') 

if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than 10')

if not(x==10):
    print(f'{x} is not equal to 10') 

numbers = [1,2,3,4,5]

if x not in numbers:
    print(x not in numbers)
else:
    print('x in numbers')

# is, is not

if x is 11:
    print(x is 11)

if x is not 10:
    print(x is not 10)