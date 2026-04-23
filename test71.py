matrix = [[1, 2, 3],
          [2, 5, 6],
          [3, 6, 9]]
symetric=True
for i in range(3):
    for j in range(3):
        if matrix[i][j]!=matrix[j][i]:
           non_symetric=False
if symetric:
    print("yes it is")
            