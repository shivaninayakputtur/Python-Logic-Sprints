# sorting|| bubble sorting
nums=[5,3,8,1,2]
for i in range(len(nums)):
    for j in range(len(nums)-1):#(3)
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
        print(nums)
