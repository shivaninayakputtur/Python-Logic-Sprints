matrix = [[1, -2, 3],
          [-4, 5, -6],
          [7, -8, 9]]
count=0
for i in matrix:
    for j in i:
        if j<0:
            count+=1
print(count)
