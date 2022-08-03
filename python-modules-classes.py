from random import randint,choice

#random is a python module written by another programmer
# randint is a function the the random module that takes in two numbers and return a random number that is between the two numbers

print(randint(1,100))

#takes a list or tuple and returns a random chosen element
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

class Die:
    def __init__(self):
        self.sides = 6
    def roll_dice(self):
        self.sides = randint(1,self.sides)
        print(f'The dice is {self.sides}')

dice_rolls = 0
while dice_rolls <=10:
    dice=Die()
    dice.roll_dice()
    dice_rolls +=1

class Lottery:
    def __init__(self):
        self.list = ['5','8','4','6','5','d','h','g','r','a']
        self.string = ''
    def lottery_winner(self):
        number =0
        while number <=8:
            choices = choice(self.list)
            self.string += choices
            number += 1
        print(self.string)

winner = Lottery()
print(winner.lottery_winner())
