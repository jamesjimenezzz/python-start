

def add_sprinkles(func):
    def wrapper(*args):
        print("*You added sprinkles*")
        func(*args)
    return wrapper

def add_fudge(func):
    def wrapper(*args):
        print("You added fudge")
        func(*args)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here's your {flavor}  ice cream")



get_ice_cream("vanilla")