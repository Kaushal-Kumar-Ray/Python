'''
List comprehensions are used for creating new lists from other iterables like lists, tuples, 
dictionaries, sets, and even in arrays and strings.
Syntax:
List = [expression(item) for item in iterable if condition]
expression: it is the item which is being iterated.
iterable: it can be list, tuples, dictionaries, sets, and even in arrays and strings.
condition: condition checks if the item should be added to the new list or not. 
Example 1: accepts items with the small letter “o” in the new list
'''
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)


#Example 2: accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_4 = [item for item in names if (len(item) > 4)]
print(namesWith_4)