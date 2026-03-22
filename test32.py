word=" I LOVE MYSELF future FAANGA employee"
word1=word.split()
result=" "
for char in word1:
    for i in range(len(char)-1,-1,-1):
        result=result+char[i]
print(result,end=" ")