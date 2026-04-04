#1.to create a function that gives sum of all numbers 
def sum_number(numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum
print(sum_number([1,2,3,4,5]))
print(sum_number([10,20,30]))

#2. reversing a list of numbers in a lists

def reversing(number):
    result=[]
    for i in range(len(number)-1,-1,-1):
        result.append(number[i])
    return result
print(reversing([1,2,3,4]))

#3.to check repeated values

def repeated(num):
    result=[]
    for item in num:
        if item not in result:
            result.append(item)
    return result
print(repeated([1,2,2,3,3,3,4,5,5]))