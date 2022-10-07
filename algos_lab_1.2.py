print("Задайте первую матрицу")
size1 = int(input()) 
matrix1 = [] 
for x in range(size1): 
    matrix1.append([int(y) for y in input().split()])

print("Задайте вторую матрицу")
size2 = int(input()) 
matrix2 = [] 
for x in range(size2): 
    matrix2.append([int(y) for y in input().split()])

print("\n")
print("Матрица 1")
for row in matrix1 :
    print(row)
print("Матрица 2")
for row in matrix2 :
    print(row)
rez = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]
print("\n","Транспонированая матрица 1")
for row in rez:
    print(row)

if len(matrix1)!=len(matrix2[0]):
    print("Матрицы не могут быть перемножены")
else:
    su=0
    v=[]
    umn=[]
    r1=len(matrix1)
    c1=len(matrix1[0])
    r2=len(matrix2)
    c2=len(matrix2[0])
    for z in range(0,r1):
        for j in range(0,c2):
            for i in range(0,c1):
                su=su+matrix1[z][i]*matrix2[i][j]
            v.append(su)
            su=0
        umn.append(v)
        v=[]
print("Умножение матриц")
for row in umn:
    print(row)



