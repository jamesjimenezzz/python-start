

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


class Cat(Animal):
    def bark(self):
        print("Meow")



dog1 = Dog("Corgi")
cat1 = Cat("Persian")

print (dog1.name)
dog1.eat()
dog1.bark()

print(cat1.name)
cat1.eat()
cat1.bark()