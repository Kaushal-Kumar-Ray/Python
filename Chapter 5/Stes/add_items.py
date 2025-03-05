'''Add items to set:
If you want to add a single item to the set use the add() method.
Example:'''
cities = {"Tokyo", "Kathmandu" ,"Delhi"}
cities.add("Madrid")
print(cities)


'''If you want to add more than one item, simply create another set or any other iterable
object(list, tuple, dictionary), and use the update() method to add it into 
the existing set.
Example:'''
cities = {"Tokyo", "Dubai", "Mosko", "Delhi"}
cities2 = {"Ohio", "Dayton", "Itahari"}
cities.update(cities2)
print(cities)