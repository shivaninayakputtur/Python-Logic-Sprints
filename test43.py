word=" aaabbbccc"
count=1
for i in range(1,len(word)):
    if word[i]==word[i-1]:
        count=count+1
    else:
        print(word[i-1],count)
        count=1
print(word[-1],count)
