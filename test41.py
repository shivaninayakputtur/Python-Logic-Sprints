word=input("enter a value")
word1=word.split()
max_length=0
max_word=" "
for word2 in word1:
    reverse=""
    for i in range(len(word2)-1,-1,-1):
        reverse=reverse+word2[i]
    if word2==reverse:
         print("palindrome")
    else:
        print("nope")
    if len(word2)>max_length:
            max_length=len(word2)
            max_word=word2
print("longest word",max_length,max_word)
        
#to check palindrome