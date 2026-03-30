#checking palindrome useing slicing
word=input("enter:")
if word==word[::-1]:
    print("palindrome")
else:
    print("nope")
# checking  a word is palindrome or not useing list +slicing
word= ["madam", "shivani", "racecar", "kiran", "noon"]
for word in word:
    if word==word[::-1]:
        print("palindrome")
    else:
        print("srry bro")