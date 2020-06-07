# Open a file

myFile = open('myfile.txt','w')

# Get some info

print('Name: ', myFile.name)
print('IsClosed: ', myFile.closed)
print('Mode: ', myFile.mode)

# Write to file

myFile.write('I love python\n')
myFile.write('and Javascript\n')
myFile.close()

# Append to file

myFile = open('myfile.txt','a')
myFile.write('I also like Rust')
myFile.close()

# Read from file

myFile = open('myfile.txt','r+')
text = myFile.read(100)
print(text)
myFile.close()


