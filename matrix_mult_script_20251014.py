import numpy as np

# Define two matrices
matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6]])

matrix_b = np.array([[7, 8],
                     [9, 10],
                     [11, 12]])

# Perform matrix multiplication using np.dot
result_dot = np.dot(matrix_a, matrix_b)

# Perform matrix multiplication using the @ operator (recommended for Python 3.5+)
result_at = matrix_a @ matrix_b

print("Matrix A:")
print(matrix_a)
print("\nMatrix B:")
print(matrix_b)
print("\nResult of A @ B (using @ operator):")
print(result_at)
print("\nResult of A.dot(B) (using np.dot):")
print(result_dot)

# Verify the results are the same
print(f"\nResults are identical: {np.array_equal(result_at, result_dot)}")
