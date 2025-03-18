'''Remove items from set:
We can use remove() and discard() methods to remove items form list.
Example 1:'''
cities={"Kathmandu", "Bhaktapur","USA","Italy"}
cities.remove("USA")
cities.discard("Italy")
print(cities)



'''
The main difference between remove and discard is that, if we try to
delete an item which is not present in set, then remove() 
raises an error, whereas discard() does not raise any error.
Example 1:'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
#cities.remove("Seoul")
cities.discard("Seoul")
print(cities)


'''
There are various other methods to remove items from the set: pop(), del(), clear().'''
#1 pop() method: we dont know which item will be removed.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(cities.pop()) # item removed
print(cities)

#2 del() method: we can remove the whole set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
#print(cities) # error

#3 clear() method: we can remove all items from the set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities) # empty set



