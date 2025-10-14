# 创建一个 3x3 的随机矩阵
A = rand(3, 3)
println("原始矩阵 A:")
display(A)

# 对矩阵 A 进行转置
A_transpose = A'
println("\n转置矩阵 A':")
display(A_transpose)

# 保存矩阵和转置矩阵到文件
writedlm("matrix_data.csv", A)
writedlm("matrix_transpose_data.csv", A_transpose)
println("\n矩阵已保存到 matrix_data.csv 和 matrix_transpose_data.csv")