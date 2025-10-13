# basic_array_ops.jl
# This script performs basic array operations like sum and mean.

# Define a sample array
arr = [1, 2, 3, 4, 5]

# Calculate the sum
total = sum(arr)
println("The sum of the array is: ", total)

# Calculate the mean
average = mean(arr)
println("The mean of the array is: ", average)

# Perform operations on a 2D array
matrix = [1 2; 3 4]
println("The 2D array (matrix) is:")
println(matrix)

# Sum of all elements in the matrix
mat_total = sum(matrix)
println("The sum of all elements in the matrix is: ", mat_total)

# Mean of all elements in the matrix
mat_mean = mean(matrix)
println("The mean of all elements in the matrix is: ", mat_mean)