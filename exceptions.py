try:
    division = 5/0
    print(division)
except ZeroDivisionError:
    print('You can not divode a number with zero')

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('Enter The First Number: ')
    if first_number == 'q':
        break
    second_number = input('Enter the second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
        print(answer)
    except:
        print('An error occured')