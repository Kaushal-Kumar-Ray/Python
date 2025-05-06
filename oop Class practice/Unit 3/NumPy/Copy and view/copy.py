import numpy as np
arr=np.array([1,2,3,4,5,6])
x=arr.copy() # Creating a copy of the array
arr[0]=10 # Modifying the original array
print(arr) # Output: [10  2  3  4  5  6]    
print(x) # Output: [1 2 3 4 5 6]    