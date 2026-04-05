# to find the missing number in a given list
def find_missing(number):
    n=len(number)+1
    expected=n*(n+1)//2
    actual=sum(number)
    return expected - actual
print(find_missing([1,2,3,5,6]))

    
