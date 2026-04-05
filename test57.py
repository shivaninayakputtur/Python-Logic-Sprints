# to check and print odd numbers in a given list
def oddnumber(numbers):
    d=[]
    for i in numbers:
        if i%2!=0:
            d.append(i)
    return d
print(oddnumber([1,2,3,4,5,6,7,8]))

# function that takes 2 lists and return common elements

def common(list1,list2):
    d=[]
    for i in list1:
        if i in list2:
            d.append(i)      
    return d
print(common([1,2,3,4,5],[3,4,5,6,7]))


            