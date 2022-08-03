bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#accessing an item
first = bicycles[0]
print(first)

#The length of the string
print(len(bicycles))

#using indiviadual values of a list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#changing a certain element
motorcycles[0] = 'ducati'
print(motorcycles)
#Removing an element from the list
#Adding an element to the end of the list
motorcycles.append('honda')
print(motorcycles)

#lopping thru a list
for bicycle in bicycles:
    print(bicycle)

#exercise-1
pizzas = ['pepperoni','bacon','cheese']
for pizza in pizzas:
    print(pizza)
print('I really love pizza')

#exercise-2
numbers = [20,85,45,68,78,44]
total = 0
for number in numbers:
    total +=number
print(total)

#exercise-3
total_range = 0
for number in range(1,100):
    total_range+=number
print(total_range)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])

#exercise -4
age_0 = 22
age_1 = 18
age = age_0 >= 21 and age_1 >=21
print(age)

#exercise-5
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

#exercise-6
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


#exercise-7
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
     print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#exercise-8
alien_color = ['green','yellow','red']
for color in alien_color:
    if(color == 'green'):
        print('You have earned 5 points')
    elif(color == 'yellow'):
        print('You have earned 10 points')
    else:
        print('You have earned 15 points')

#age exercise
age = 5
if(age<2):
    print('You are a baby')
elif(age>=2 and age<=4):
    print('You are a toddler')
elif(age>=4 and age<=13):
    print('You are a kid')
elif(age>=13 and age<=20):
    print('You are a teenger')
elif(age>=20 and age<=65):
    print('You are an adult')
    
#pizza exercise
#checking if the requested toppings are in stock
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested in requested_toppings:
    if(requested in available_toppings):
        print(f"Adding {requested} to pizza")
    else:
        print(f'{requested} is not availble')

# users exercises
usernames = ['fridah','emily','anna','frimogen','admin']
if(usernames):
    for user in usernames:
        if (user == 'admin'):
            print(f"Hello {user} would you like a status report")
        else:
            print(f"Hello {user} welcome back")
else:
    print('There are no available users')

#checking usernames
current_users = ['fridah','emily','anna','frimogen','admin']
new_users = usernames = ['mary','jackie','jane','Frimogen','admin']
for user in new_users:
    if user.lower() in current_users:
        print(f'{user} has already been taken')
    else:
        print(f'{user} is availble')

ordinal_numbers = [1,2,3,4,5,6,7,8,9]
for number in ordinal_numbers:
    if(number == 1):
        print(f'{number}st')
    elif(number == 2):
        print(f'{number}nd')
    elif(number == 3):
        print(f'{number}rd')
    else:
        print(f'{number}th')
