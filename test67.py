matrix = [[3, 7, 1],
          [9, 2, 6],
          [4, 8, 5]]
for row in matrix:
    smallest=row[0]
    for j in row:
        if j<smallest:
            smallest=j
    print(smallest)
# to get sum of each cloumn
nums= [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for j in range(3):
    column=0
    for i in range(3):
        column=column+nums[i][j]
    print(column)