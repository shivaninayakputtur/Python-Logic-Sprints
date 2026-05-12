# Count occurrences of target in sorted list!
nums = [1, 3, 3, 5, 5, 5, 8, 9]
target = 5
left=0
right=len(nums)-1
result1=-1
result2=-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        result1=mid
        right=mid-1
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
left=0
right=len(nums)-1
result2=-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        result2=mid
        left=mid+1
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
print(result2-result1+1)