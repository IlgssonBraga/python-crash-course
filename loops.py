people = ['Ilgsson', 'Ilgner', 'Katia', 'Arlaine']

# for

for person in people:
    print(person)

# break

for person in people:
    if person == 'Katia':
        break
    print(person)

# continue


for person in people:
    if person == 'Katia':
        continue
    print(person)

print('')

# range

for i in range(len(people)):
    print(people[i])

print('')

for i in range(0, 11):
    print(f'Number: {i}')

print('')

# while

count = 0

while count <= 10:
    print(f'Count: {count}')
    count += 1