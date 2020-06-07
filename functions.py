# Create function

def sayHello(name=''):
    print(f'Hello {name}')

sayHello()

# Return values

def sum(num1, num2):
    total = num1 + num2
    return total

num = sum(3,2)
print(num)

# Lambda functions

getSum = lambda num1, num2 : num1 + num2

print(getSum(3,3))