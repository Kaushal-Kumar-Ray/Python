'''Changing items from list is easier, you just have to specify the index where you want 
to replace the item with existing item.
Example:'''
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Millie"
print(names)
names[2:4] = ["juan", "Anastasia"]
print(names)

'''
What if the range of the index is more than the list of items provided?
In this case, all the items within the index range of the original list 
are replaced by the items that are provided.
Example:
'''
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[1:4] = ["juan", "Anastasia"]
print(names)

'''
What if we have more items to be replaced than the index range provided?
In this case, the original items within the range are replaced by the 
new items and the remaining items move to the right of the list accordingly.
Example:
'''
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2:3] = ["juan", "Anastasia", "Bruno", "Olga", "Rosa"]
print(names)