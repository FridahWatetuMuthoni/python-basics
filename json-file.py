import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as file:
    json.dump(numbers, file)


with open(filename) as file:
    numbers = json.load(file)

print(numbers)

# saving and reading user generated data
print("Type 'q' to quit the program")
names = []
index = 0

while True:
    name = {}
    username = input('Please enter your name: ')
    if username:
        if username.lower() == 'q':
            print('Program Ended')
            break
        else:
            name[index] = username

    filename = 'users.json'
    names.append(name)
    index += 1

    with open(filename, 'w') as file:
        json.dump(names, file)

    with open(filename) as file:
        names = json.load(file)
        for user in names:
            print(user)
