matrix = [[1, -2, 3],
          [-4, 5, -6],
          [7, -8, 9]]
for i in range(3):
    for j in range(3):
        if matrix[i][j]<0:
            matrix[i][j]=0
        print(matrix[i][j])
# rotate values to 90
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for i in range(3):
    for j in range(3):
        matrix[i][j]=matrix[j][i]
    print(matrix[i][j])