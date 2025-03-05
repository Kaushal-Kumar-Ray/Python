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