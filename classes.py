# Create class

class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def hasBirthday(self):
        self.age += 1

# Init user object

user1 = User('Ilgsson', 'ilgsson@live.com', 25)

print(type(user1))
print(user1.name, user1.email, user1.age)
user1.hasBirthday()

print(user1.greeting())

# Extend class

class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init customer object

customer1 = Customer('Ilgner', 'ilgnerbraga@gmail.com', 25)

print(customer1.balance)

customer1.set_balance(10)

print(customer1.balance)

customer1.hasBirthday()

print(customer1.greeting())

