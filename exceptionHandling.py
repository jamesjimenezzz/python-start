

try:
    number = int(input("Enter a number: "))
    print(2/number)
except ZeroDivisionError:
    print("You cant divide by number 0")
except ValueError:
    print("Enter only a number pleasee")
except Exception:
    print("Something went wrong")
finally:
    print("Add a cleanup here.")