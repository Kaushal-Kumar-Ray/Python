import numpy as np
import time

def separator(title):
    """Print a section separator with a title."""
    print("\n" + "=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50 + "\n")

# SECTION 1: Creating NumPy Arrays
separator("1. CREATING NUMPY ARRAYS")

# 1.1 Creating arrays from Python lists
print("1.1 Creating arrays from Python lists:")
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(f"1D array: {array_1d}")
print(f"2D array:\n{array_2d}")
print(f"3D array:\n{array_3d}")

# 1.2 Creating arrays with special values
print("\n1.2 Creating arrays with special values:")
zeros = np.zeros((2, 3))
ones = np.ones((2, 2))
identity = np.eye(3)
empty = np.empty((2, 2))  # Uninitialized values (whatever is in memory)

print(f"Zeros:\n{zeros}")
print(f"Ones:\n{ones}")
print(f"Identity matrix:\n{identity}")
print(f"Empty (uninitialized):\n{empty}")

# 1.3 Creating arrays with sequences
print("\n1.3 Creating arrays with sequences:")
range_array = np.arange(0, 10, 2)  # start, stop, step
linspace = np.linspace(0, 1, 5)    # start, stop, num of points
logspace = np.logspace(0, 3, 4)    # 10^0 to 10^3, 4 points

print(f"Range (arange): {range_array}")
print(f"Linear space: {linspace}")
print(f"Log space: {logspace}")

# 1.4 Creating random arrays
print("\n1.4 Creating random arrays:")
random_uniform = np.random.rand(3, 3)     # Uniform [0,1)
random_normal = np.random.randn(3, 3)     # Standard normal
random_int = np.random.randint(0, 10, (3, 3))  # Random integers

print(f"Random uniform [0,1):\n{random_uniform}")
print(f"Random normal (mean=0, std=1):\n{random_normal}")
print(f"Random integers [0,10):\n{random_int}")

# SECTION 2: Array Attributes and Information
separator("2. ARRAY ATTRIBUTES AND INFORMATION")

sample_array = np.array([[1, 2, 3], [4, 5, 6.5]])
print(f"Sample array:\n{sample_array}")
print(f"Shape: {sample_array.shape}")
print(f"Dimensions: {sample_array.ndim}")
print(f"Size (total elements): {sample_array.size}")
print(f"Data type: {sample_array.dtype}")
print(f"Item size (bytes): {sample_array.itemsize}")
print(f"Total bytes: {sample_array.nbytes}")

# SECTION 3: Array Indexing and Slicing
separator("3. ARRAY INDEXING AND SLICING")

array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"Original 2D array:\n{array_2d}")

# 3.1 Basic indexing
print("\n3.1 Basic indexing:")
print(f"Element at (0,0): {array_2d[0, 0]}")
print(f"Element at (2,3): {array_2d[2, 3]}")

# 3.2 Slicing
print("\n3.2 Slicing:")
print(f"First row: {array_2d[0, :]}")
print(f"First column: {array_2d[:, 0]}")
print(f"Submatrix (first 2 rows, first 3 columns):\n{array_2d[0:2, 0:3]}")

# 3.3 Advanced indexing
print("\n3.3 Advanced indexing:")
# Boolean indexing
print("Elements greater than 5:")
print(array_2d[array_2d > 5])

# Integer array indexing
row_indices = np.array([0, 1, 2])
col_indices = np.array([0, 2, 3])
print("Elements at positions (0,0), (1,2), (2,3):")
print(array_2d[row_indices, col_indices])

# SECTION 4: Array Manipulation
separator("4. ARRAY MANIPULATION")

# 4.1 Reshaping
print("4.1 Reshaping:")
arr = np.arange(12)
print(f"Original array: {arr}")
reshaped = arr.reshape(3, 4)
print(f"Reshaped to 3x4:\n{reshaped}")
print(f"Reshaped to 3x2x2:\n{arr.reshape(3, 2, 2)}")

# 4.2 Transposing
print("\n4.2 Transposing:")
print(f"Original 2D array:\n{reshaped}")
print(f"Transposed array:\n{reshaped.T}")

# 4.3 Flattening and ravel
print("\n4.3 Flattening and ravel:")
print(f"Flattened array: {reshaped.flatten()}")
print(f"Raveled array: {reshaped.ravel()}")

# 4.4 Stacking arrays
print("\n4.4 Stacking arrays:")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(f"Array a:\n{a}")
print(f"Array b:\n{b}")
print(f"Vertical stack:\n{np.vstack((a, b))}")
print(f"Horizontal stack:\n{np.hstack((a, b))}")
print(f"Column stack:\n{np.column_stack((a[:, 0], b[:, 0]))}")

# 4.5 Splitting arrays
print("\n4.5 Splitting arrays:")
big_array = np.arange(16).reshape(4, 4)
print(f"Original array:\n{big_array}")
print("Split horizontally into 2 parts:")
for part in np.hsplit(big_array, 2):
    print(part)
print("Split vertically into 2 parts:")
for part in np.vsplit(big_array, 2):
    print(part)

# SECTION 5: Mathematical Operations
separator("5. MATHEMATICAL OPERATIONS")

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(f"Array a: {a}")
print(f"Array b: {b}")

# 5.1 Basic operations
print("\n5.1 Basic operations:")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a ** 2 = {a ** 2}")
print(f"sqrt(a) = {np.sqrt(a)}")

# 5.2 Linear algebra
print("\n5.2 Linear algebra:")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"Matrix A:\n{A}")
print(f"Matrix B:\n{B}")
print(f"Matrix multiplication (A @ B):\n{A @ B}")
print(f"Matrix multiplication (np.matmul):\n{np.matmul(A, B)}")
print(f"Matrix multiplication (np.dot):\n{np.dot(A, B)}")

# Determinant, inverse, etc.
print(f"Determinant of A: {np.linalg.det(A)}")
print(f"Inverse of A:\n{np.linalg.inv(A)}")
print(f"Eigenvalues of A: {np.linalg.eigvals(A)}")

# 5.3 Statistical functions
print("\n5.3 Statistical functions:")
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Data: {data}")
print(f"Mean: {np.mean(data)}")
print(f"Median: {np.median(data)}")
print(f"Standard deviation: {np.std(data)}")
print(f"Variance: {np.var(data)}")
print(f"Min: {np.min(data)}")
print(f"Max: {np.max(data)}")
print(f"Sum: {np.sum(data)}")
print(f"Cumulative sum: {np.cumsum(data)}")

# 5.4 Trigonometric functions
print("\n5.4 Trigonometric functions:")
angles = np.array([0, np.pi/4, np.pi/2, np.pi])
print(f"Angles: {angles}")
print(f"sin(angles): {np.sin(angles)}")
print(f"cos(angles): {np.cos(angles)}")
print(f"tan(angles): {np.tan(angles)}")

# SECTION 6: Broadcasting
separator("6. BROADCASTING")

# Broadcasting allows operations on arrays of different shapes
a = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3 array
b = np.array([10, 20, 30])            # 1D array
print(f"Array a (2x3):\n{a}")
print(f"Array b (1D): {b}")
print(f"a + b (broadcasting):\n{a + b}")

# Broadcasting with scalar
print(f"a + 100:\n{a + 100}")
print(f"a * 2:\n{a * 2}")

# SECTION 7: Performance Comparison with Python Lists
separator("7. PERFORMANCE COMPARISON")

size = 1000000
list_start = time.time()
py_list = list(range(size))
py_result = [x**2 for x in py_list]
list_time = time.time() - list_start

numpy_start = time.time()
np_array = np.arange(size)
np_result = np_array**2
numpy_time = time.time() - numpy_start

print(f"Time to square {size} elements:")
print(f"Python list: {list_time:.6f} seconds")
print(f"NumPy array: {numpy_time:.6f} seconds")
print(f"NumPy is {list_time / numpy_time:.1f}x faster")

# SECTION 8: Saving and Loading Arrays
separator("8. SAVING AND LOADING ARRAYS")

# Create a sample array
sample = np.random.rand(3, 4)
print(f"Original array:\n{sample}")

# Save to binary file
np.save('sample_array.npy', sample)
print("Array saved to 'sample_array.npy'")

# Load from binary file
loaded = np.load('sample_array.npy')
print(f"Loaded array:\n{loaded}")

# Save multiple arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.savez('multiple_arrays.npz', a=a, b=b)
print("Multiple arrays saved to 'multiple_arrays.npz'")

# Load multiple arrays
loaded_npz = np.load('multiple_arrays.npz')
print(f"Loaded array 'a': {loaded_npz['a']}")
print(f"Loaded array 'b': {loaded_npz['b']}")

# Text format
np.savetxt('array.csv', sample, delimiter=',')
print("Array saved to 'array.csv'")
loaded_txt = np.loadtxt('array.csv', delimiter=',')
print(f"Loaded from CSV:\n{loaded_txt}")

# SECTION 9: Advanced Features
separator("9. ADVANCED FEATURES")

# 9.1 Masked arrays
print("9.1 Masked arrays:")
data = np.array([1, 2, 3, -999, 5, 6, -999, 8])
print(f"Original data: {data}")
masked_data = np.ma.masked_array(data, mask=(data == -999))
print(f"Masked data: {masked_data}")
print(f"Mean of masked data: {masked_data.mean()}")

# 9.2 Structured arrays
print("\n9.2 Structured arrays:")
dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
people = np.array([
    ('Alice', 25, 55.0),
    ('Bob', 32, 75.5),
    ('Charlie', 45, 80.2)
], dtype=dt)
print(f"Structured array:\n{people}")
print(f"Names: {people['name']}")
print(f"Ages: {people['age']}")
print(f"Mean age: {people['age'].mean()}")

# 9.3 Universal functions (ufuncs)
print("\n9.3 Universal functions (ufuncs):")
data = np.arange(1, 6)
print(f"Data: {data}")
print(f"np.add.reduce(data): {np.add.reduce(data)}")  # Same as sum
print(f"np.multiply.reduce(data): {np.multiply.reduce(data)}")  # Same as product
print(f"np.add.accumulate(data): {np.add.accumulate(data)}")  # Same as cumsum

# 9.4 Fancy indexing example - the Mandelbrot set
print("\n9.4 Fancy indexing example - the Mandelbrot set:")
def mandelbrot(h, w, max_iter):
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x + y*1j
    z = c
    divtime = max_iter + np.zeros(z.shape, dtype=int)
    
    for i in range(max_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == max_iter)
        divtime[div_now] = i
        z[diverge] = 2
    
    return divtime

# Setting small values for quick computation
h, w = 30, 50
max_iter = 20
plt = mandelbrot(h, w, max_iter)
print("Simple ASCII Mandelbrot set:")
for row in plt:
    print(''.join(' .:-=+*#%@'[int(min(cell * 10 // max_iter, 9))] for cell in row))
