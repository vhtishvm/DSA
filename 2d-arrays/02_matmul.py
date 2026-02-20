import time

matrix1 = [[1,2],
           [3,4]]

matrix2 = [[5,6],
           [7,8]]

matrix3 = [[0,0],
           [0,0]]

row_1 = len(matrix1)
column_1 = len(matrix1[0])
row_2 = len(matrix2)
column_2 = len(matrix2[0])
start = time.time()


for i in range(row_1):
    for j in range(column_2):
        for k in range(row_2):
            matrix3[i][j] += matrix1[i][k]*matrix2[k][j]


end = time.time()
print(f"Function executed in time: {end-start}")
print(matrix3)




