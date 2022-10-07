import numpy as np

print("Задайте первую матрицу")
size1 = int(input()) 
matrix1 = [] 
for x in range(size1): 
    matrix1.append([int(y) for y in input().split()])
matrix1=np.array(matrix1)

print("Задайте вторую матрицу")
size2 = int(input()) 
matrix2 = [] 
for x in range(size2): 
    matrix2.append([int(y) for y in input().split()])
matrix1=np.array(matrix1)

sum=matrix1.dot(matrix2)
print("Умножение матриц: \n",sum)

tran=(matrix1.transpose())
print("Транспонированая матрица 1 \n",tran)

r = np.linalg.matrix_rank(matrix1)
print("Ранг матрицы 1:",r)
