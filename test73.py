matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
sum=1
for row in matrix:
    for j in row:
        sum=sum*j
print(sum)