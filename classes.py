"""_summary_
Making an object from a class is called instantiation, and you work with 
instances of a class. 

The __init__() Method
A function that is part of a class is a method
"""

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f'{self.name} is now sitting')
    
    def roll_over(self):
        print(f"{self.name} rolled over!")

dog_one = Dog('Baby',12)
dog_one.sit()
dog_one.roll_over()


class Restaurant:
    def __init__(self,type,cuisine):
        self.type=type
        self.cuisine = cuisine
        self.served = 0
    
    def describe_restaurant(self):
        print(f'Our {self.type} restaurant sells only {self.cuisine}')
    
    def open_restaurant(self):
        print('The restaurant is now open')   
    
    def number_served(self,customers):
        self.served += customers 

new_rest = Restaurant('Bed and Breakfast','sausage and bacon')
print(new_rest.type)
print(new_rest.cuisine)
new_rest.describe_restaurant()
new_rest.number_served(10)
new_rest.number_served(5)
print(new_rest.served)


class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        #setting a default value for our class
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model} {self.odometer_reading}'
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mirage):
        if(mirage >=self.odometer_reading):
            self.odometer_reading = mirage
        else:
            print('you cant roll back the odometer')
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles




new_car = Car('audi','a4', 2019)
new_car.update_odometer(20)
print(new_car.get_descriptive_name())
print(new_car.read_odometer())

#CLASS INHERITANCE
"""""
Class inhertance is when a class inherits all the properties and methods from another class
The class that is inhereted from is called the paerent and the class that
inherits it is called the child.The child class inherits everthing and it can
also add mor custom methods and properties
the super() method is a special function that allows you to call a method from the parent class
When you use inheritance you can make your child classses retain what you need
and override anything that you dont need from the parent class
"""
class Battery:
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")
        
class EletricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
    

my_tesla = EletricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

class IceCreamStand(Restaurant):
    def __init__(self, type, cuisine,*flavour):
        self.flavour = flavour
        super().__init__(type, cuisine)
    def our_flavours(self):
        print(f'Our flavours include the following {self.flavour}')

iceCream = IceCreamStand('icecream','all_creams','strawberries','vannilla','chocolate')
iceCream.our_flavours()

