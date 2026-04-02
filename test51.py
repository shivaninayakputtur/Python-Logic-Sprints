# to find largest number in a given list
def largest(word):
    max_count=0
    for i in word:
        if i>max_count:
            max_count=i
    return max_count
print(largest([7,9,3,2]))

#to find average of a given number in a list
 
def average(number):
    sum=0
    for i in number:
        sum=sum+i
        average=sum/len(number)
    return average
print(average([5,1]))
