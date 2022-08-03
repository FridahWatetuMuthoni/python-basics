filename_1 = 'text.txt'

number_of_help_in_file = 0

with open(filename_1) as file:
    for line in file:
        new_line = line.strip().split(" ")
        if 'help' in new_line:
            number_of_help_in_file += 1

print(number_of_help_in_file)


print("############################################")

filename_2 = 'large.txt'

with open(filename_2) as file:
    lines = file.readlines()

the = 0
for line in lines:
    if 'the' in line:
        the += 1
print(the)

print("############################################")

# openning the file in write mode
filename_3 = 'write.txt'

with open(filename_3, 'w') as file:
    file.write('I love programming because it is not boring \n')
    file.write("I love creating new games.")


# openning the file in append mode.appends the file instead of overridding it
with open(filename_3, 'a') as file:
    file.write('I love watching movies because its very entertaing')

print('Please enter your name so that we can add it in the quest list')
print("Enter 'q' if you want to quit the program")
number_of_guest = 1
while True:
    name = input('Please Enter Your name: ')
    if name:
        if name.lower() == 'q':
            break
        else:
            with open('guest.txt', 'a') as file:
                file.write(f'{number_of_guest}. Name: {name} \n')
                number_of_guest += 1
            print(f'Hello {name} welcome to our hotel')

# working with multpile files


def count_words(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, The file {filename} does not exist")
    else:
        words = contents.split()
        total = len(words)
        print(f"The file {filename} has about {total} words")


files = ['write.txt', 'large.txt', 'quest.txt', 'text.txt']
for file in files:
    count_words(file)
