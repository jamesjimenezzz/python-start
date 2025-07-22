
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]


groceries = [fruits, vegetables, meats]


for grocery in groceries:
    for food in grocery:
        print(food, end=" ")
    
    print() 



#--NUMPAD-----------


col1 = (1, 2, 3)
col2= (4,5,6)
col3= (7,8,9)
col4 = ("*", 0, "#")

all_columns = (col1, col2, col3, col4)

for i in all_columns:
    print()
    for j in i:
        print(j, end=" ")