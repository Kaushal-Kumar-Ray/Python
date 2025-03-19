'''• isdisjoint():
The isdisjoint() method checks if items of given set are present in another set.
This method returns False if items are present, else it returns True.
Example 1:'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))


'''• issuperset():
The issuperset() method checks if all the items of a particular set are present in 
the original set. It returns True if all the items are present, else it returns False.
Example 1:'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))
cities4 = {"Delhi", "Madrid"}
print(cities.issuperset(cities4))


'''
• issubset():
The issubset() method checks if all the items of the original set are present in the
particular set. It returns True if all the items are present, else it returns False.
Example 1:'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities4 = {"Delhi", "Madrid"}
print(cities4.issubset(cities))
cities2 = {"Seoul", "Kabul"}
print(cities2.issubset(cities))
cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities3.issubset(cities))