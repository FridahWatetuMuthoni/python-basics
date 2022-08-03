#age =input('Enter your age: ')
age=10
if(int(age) >= 18):
    print('You are old enough to vote')
else:
    print('You are too young to vote')


#we are only dealing with odd numbers and ignoring the even numbers
current_number = 0
while current_number <10:
    current_number += 1
    if (current_number % 2 == 0):
        continue
    print(current_number)

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#checking if there is a user in the unconfirmed_users
while unconfirmed_users:
    #removing the last user in the list
    current_user = unconfirmed_users.pop()
    #adding the removed user to the comfirmed lis
    confirmed_users.append(current_user)
#printing all the confirmed users
print(confirmed_users)
print(unconfirmed_users)