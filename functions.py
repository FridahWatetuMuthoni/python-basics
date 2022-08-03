def greet_user(user):
    print(f'Hello {user}')

print(greet_user('Anna'))

#returns a tuple of all the arguements hat were passed in the function
def names(*args):
    print(args)

names('anna','mary','jane','emily')

#arbitary arguements (*args), arbitary keyword arguements (**kwargs)
"""
The double asterisks before the args = **args causes python to create an empty
dictionary which is used to store all of the arbitary arguements
we then add our positional arguements to this list then return it
"""

def build_profile(first, last, **args):
    """Build a dictionary containing everything we know about a user."""
    args['first_name'] = first
    args['last_name'] = last
    return args

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)

