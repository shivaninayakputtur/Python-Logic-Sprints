#rotation of numbers
def rotate(number,k):
    return number[-k:]+number[:-k]
print(rotate([1,2,3,4,5],2))

# making a sublist into a complete lists

def flatten(lists):
    result= []
    for sublists in lists:
        for item in sublists:
            result.append(item)
    return result
print(flatten([[1,2],[3,4],[5,6]]))