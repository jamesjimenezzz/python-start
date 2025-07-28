

#add_1 = lambda x,y : x + y

#result = add_1(5,5)

#print(result)

my_numbers=[1,2,3,4,5,6,7,8,9,10]


results = list(filter(lambda x: x % 2 == 0, my_numbers))
print(results)