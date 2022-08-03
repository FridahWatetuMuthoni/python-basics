from funcs import formated_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    name  = formated_name(first,last)
    print(f'Our well formatted name is {name}')
    break