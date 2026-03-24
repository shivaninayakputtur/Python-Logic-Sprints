word=" i love programming and myself"

result=" "

for char in word:

    if char!=" ":

        result=result+char

print(result)
#toprint words without spaces
# toprint words tht start with vowels 

word=" i am a good programmer and engineer"
word1=word.split()

count=0

for char in range(len(word1)):
    
    if word1[char][0]=="a" or word1[char][0]=="e" or word1[char][0]=="i" or word1[char][0]=="o" or word1[char][0]=="u":

        count=count+1

print(count)
