matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
n=int(input("enter:"))
r=[]
for row in matrix:
    i=0
    for col in row:
        if col == n:
            r.append(col)
print(r)
# 
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for i in range(3):
    print(matrix[i][i])

