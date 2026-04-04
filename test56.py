# to find the second largest number in a given list
def second_largest(number):
    max_second=""
    largest=0
    second=0
    for item in number:
        if item>largest:
            largest=item
    for item in number:
        if item>second and item<largest:
            second=item
    return second
print(second_largest([1,4,6,9,3,2]))