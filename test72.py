# printing numbers above the daigonal
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for i in range(3):
    for j in range(3):
        if j>i:
            print(matrix[i][j])
# print numbers below the daigonals
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for i in range(3):
    for j in range(3):
        if i>j:
            print(matrix[i][j])
