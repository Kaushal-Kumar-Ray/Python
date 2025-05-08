import numpy as np

# Create a 1D array with 12 random values between 0 and 1
random = np.random.rand(12)
print("Randomly generated array:\n", random)


arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Original array:\n", arr)
reshaped = arr.reshape((3, 4))  # This is probably what you meant by reshapea()
print("\nReshaped to 3x4:\n", reshaped)

# Calculate mean of the whole array
mean_val = np.mean(reshaped)
print("\nMean of array:", mean_val)

# Calculate the maximum value
max_val = np.max(reshaped)
print("Max value in array:", max_val)

# Calculate standard deviation
std_val = np.std(reshaped)
print("Standard deviation:", std_val)

# Calculate sum of all elements
sum_val = np.sum(reshaped)
print("Sum of all elements:", sum_val)

# Create another array of same shape and concatenate along axis 0
arr2 = np.array([[13,14,15,16],[17, 18,19,20]])
concatenated = np.concatenate((reshaped, arr2))
print("\nConcatenated array (along rows):\n", concatenated)
