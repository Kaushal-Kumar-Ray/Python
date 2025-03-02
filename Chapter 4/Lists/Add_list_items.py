'''
append():
This method appends items to the end of the existing list.

Example:
'''
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)

'''insert():
This method inserts an item at the given index. 
User has to specify index and the item to be inserted within the insert() method.

Example:
'''
colors = ["voilet", "indigo", "blue"]
colors.insert(1, "green")   
print(colors)

'''
extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

Example 1:
'''
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

#add a tuple to a list
cars = ["Hyundai", "Tata", "Mahindra"]
cars2 = ("Mercedes", "Volkswagen", "BMW")
cars.extend(cars2)
print(cars)

#add a set to a list
fruits = ["apple", "banana", "mango"]
fruits2 = {"orange", "grapes", "kiwi"}
fruits.extend(fruits2)
print(fruits)

#add a dictionary to a list
vegetables = ["carrot", "potato", "onion"]
vegetables2 = {"tomato": 10, "cucumber": 5, "capsicum": 3}
vegetables.extend(vegetables2)
print(vegetables)

'''
concatenate two lists:
you can simply concatenate two list to join two lists.

Example:
'''
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
