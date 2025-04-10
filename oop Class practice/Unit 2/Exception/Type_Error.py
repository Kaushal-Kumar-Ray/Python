p=5
try:
    x=int(p)
except TypeError:
    print("TypeError: p is not an integer")
print("Bye")


'''
p="5"
try:
    x=int(p)
except TypeError:
    print("TypeError: p is not an integer")  #output
print("Bye")
'''