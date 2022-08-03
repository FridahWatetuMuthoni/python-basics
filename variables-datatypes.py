#VARIABLES
greeting = 'Hello World with variable'

try:
    print(greeting)
except NameError:
    print('There was an error when printing greating')
finally:
    print('Executes where there is an error or not')

#STRINGS
message = 'This is my new message';
print(message)

new_message = message

#everything is lowercase
print(new_message.lower())
#everything is uppercase
print(new_message.upper())
#every word is capitalized
print(new_message.title())

first_name = 'ada'
last_name = 'lovelace'

print(f'The full name is {first_name} {last_name}')

#Using tabs
print(f"\t {first_name}")

#using new line
print('This are some of the programming languages: \n Javascript \n Pyhton \n C++ \n Java')

#using new line and tabs together
print("Languages:\n\tPython \n\tC \n\tJavaScript") 

#stripping whitespace (both right and left)
language = ' Python '
#with white space
print(language)
#without white space
print(language.strip())

#NUMBERS

#integers
num1 = 10
num2=14
print(num1 + num2)

#floating point numbers
float1 = 2.2
float2 = 4.6
print(float1 + float2)

# BODMAS(order of operations) brackets,of ,division,multiplication, addition and subtractions

