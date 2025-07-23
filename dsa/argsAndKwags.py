

def display_name(*args):
    for arg in args:
        print(arg, end=", ")



display_name("James Jimenez", "Simon Cancino")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")




print_address(street="123", brgy="Pob.Norte" )



def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    print(f"{kwargs.get("street")} {kwargs.get("province")}")




shipping_label("James", "Jimenez", street="Daniel Maramba", province="Pagansinan")