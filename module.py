def make_pizza(size,*args):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in args:
        print(f'-{topping}')
