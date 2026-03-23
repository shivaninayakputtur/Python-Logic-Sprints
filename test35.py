word="i love python i love python i love faang"
word1=word.split()
d={}
for  char in word1:
    if char in d:
        d[char]=d[char]+1
    else:
        d[char]=1
for key in d:
    print(key)


        