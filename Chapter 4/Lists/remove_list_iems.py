'''pop():
This method removes the last item of the list if no index is provided. 
If an index is provided, then it removes item at that specified index.
Example 1:
'''
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop()        #removes the last item of the list
print(colors)
colors.pop(1)       #removes item at index 1
print(colors)


'''
remove():
This method removes specific item from the list.
Example:
'''
colors = ["voilet", "indigo", "blue", "green", "yellow"]
colors.remove("blue")
print(colors)


'''
del:
del is not a method, rather it is a keyword which 
deletes item at specific from the list, or deletes the list entirely.
Example 1:
'''
colors = ["voilet", "indigo", "blue", "green", "yellow"]
del colors[3]
print(colors)
'''del colors
print(colors)'''  #this will raise an error as the list is deleted

'''clear():
This method clears all items in the list and prints an empty list.
Example:
'''
colors = ["voilet", "indigo", "blue", "green", "yellow"]
colors.clear()
print(colors)