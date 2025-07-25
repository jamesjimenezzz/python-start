

class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating now.")
    
    def sleep(self):
        print(f"{self.name} is sleeping now.")

    
class Dog(Animal):
    def bark(self):
        print("Woof")



dog1 = Dog("Corgi")


print (dog1.name)
dog1.eat()
dog1.bark()