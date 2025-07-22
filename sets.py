

utensils = {"fork", "knife", "spoon"}
dishes = {"steak", "adobo", "sisig"}

#utensils.add("add1")
#utensils.remove("add1")
#utensils.clear()
#utensils.update(dishes)

mainSet = utensils.union(dishes)


for i in mainSet:
    print(i)