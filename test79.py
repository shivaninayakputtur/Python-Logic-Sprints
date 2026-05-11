# binary search 
num=[1,2,3,5,8,9,11]
target=8
left=0 # element start with index=0
right=len(num)-1 # so here length=7 but i=0 so 7-1=6
while left<=right:
    mid=(left+right)//2
    if num[mid]==target:
        print("found")
        break
    elif num[mid] < target:
        left=mid+1
    else:
        right=mid-1
