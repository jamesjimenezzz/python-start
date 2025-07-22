
 #---------- Array
fruits = ["apple", "orange", "banana", "coconut"]

fruits.insert(0, "pineapple")
fruits.sort( )

for fruit in fruits:
    
    print(fruit)



#------Sets

fruits ={"apple", "orange", "blueberry", "banana"}
fruits.add("addedFruit")
fruits.remove("apple")
fruits.pop()


for fruit in fruits:
    print(fruit)




#---------Tuple

fruits = ("apple", "orange", "blueberry", "cheesecake")

print(fruits.index("apple"))