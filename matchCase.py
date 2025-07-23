

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday":
            return False
        case _:
            return "Invalid"




x = input("Determine if its weekend: ")



y = is_weekend(x.capitalize())

print(y)