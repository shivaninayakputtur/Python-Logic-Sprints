word=input("enter the sentence:")
word1=word.split()
count=0
for word in word1:
    count=0# bcs it starts ecah loop with new numners doesnt requests each with 1 word
    for char in word:
        if char in "aeiou":
            count=count+1
    print(word,"appears",count,"times")