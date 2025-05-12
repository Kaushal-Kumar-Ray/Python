
import numpy as np
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the elements of the matrix row-wise:")
matrix = []
for i in range(rows):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    matrix.append(row)

A = np.array(matrix)
Q, R = np.linalg.qr(A)

print("\nOriginal Matrix A:")
print(A)

print("\nOrthogonal Matrix Q:")
print(Q)

print("\nUpper Triangular Matrix R:")
print(R)