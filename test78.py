num=[5,3,8,1,2]
target=8
found=False
for i in range(len(num)):
    if num[i]==target:
        found=True
        print("found at index",i)
if not found:
    print("not found")

