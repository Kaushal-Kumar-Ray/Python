'''
Tuple Indexes
Each item/element in a tuple has its own unique index. This index can be used to 
access any particular item from the tuple. The first item has
index [0], second item has index [1], third item has index [2] and so on.
Example:
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]'''

#Accessing tuple items:
''' I. Positive Indexing: and II Negative Indexing'''
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[1])
print(country[3])
print(country[0])
print(country[-1])
print(country[-3])
print(country[-4])



'''
III. Check for item:
We can check if a given item is present in the tuple. This is done using the in keyword.
Example 1:'''

country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
    
    
    
    
'''
IV. Range of Index:
You can print a range of tuple items by specifying where do you want to start, 
where do you want to end and if you want to skip elements in between the range.
Syntax:
Tuple[start : end : jumpIndex]
Note: jump Index is optional. We will see this in given examples.'''        

'''Example:1 printing elements within a particular range:'''
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes


'''Example: printing all element from a given index till the end'''
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes

'''Example: printing all elements from start to a given index'''
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes

'''Example: print alternate values'''
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes     -8 , -6, -4, -2

'''Example: printing every 3rd consecutive withing given range'''
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])