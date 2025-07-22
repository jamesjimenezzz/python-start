
capitals = {"USA": "Washington D.C", "India": "New Delhi", "China": "Beijing"}

capitals.update({"Germany": "Berlin"})

# print(capitals["USA"])

#print(capitals.get('USA')) #Much checker with error handling



for key, values in capitals.items():
    print(key, values)