num= [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
sum=0
for i in num:
    for j in i:
        sum=sum+j
print(sum)
# to find largest number in a given 2D array
nums= [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
largest=0
for i in nums:
    for j in i:
        if j>largest:
            largest=j
print(largest)
