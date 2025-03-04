'''sort(): This method sorts the list in ascending order.
Example 1:
'''
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
print("for descending order")
colors.sort(reverse=True)
print(colors)
num.sort(reverse=True)      
print(num)

'''reverse(): This method reverses the order of the list. 
Example:
'''
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

'''
index(): This method returns the index of the first occurrence of the list item.
Example:
'''
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))



'''
count(): Returns the count of the number of items with the given value.
Example:
'''
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]


'''
copy(): Returns copy of the list. This can be done to perform operations on the 
list without modifying the original list. 
Example:
'''
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)