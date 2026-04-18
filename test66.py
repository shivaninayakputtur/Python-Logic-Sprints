# to find sum of each row
nums= [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for i in nums:
    row=0
    for j in i:
        row=row+j
    print(row)

# to check even or odd

nums= [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
even_count=0
odd_count=0
for i in nums:
    for j in i:
        if j%2==0:
            even_count=even_count+1
        else:
            odd_count=odd_count+1
print(even_count)
print(odd_count)