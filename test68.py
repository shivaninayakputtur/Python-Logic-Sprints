nums= [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
result = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(nums[j][i])
    result.append(row)
print(result)