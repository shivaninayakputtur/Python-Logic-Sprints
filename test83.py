nums = [1, 3, 5, 7, 9]
sorted = True
for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        sorted = False
if sorted:
    print("Sorted!")
else:
    print("Not Sorted!")