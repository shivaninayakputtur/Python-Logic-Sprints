word= input("enter the name")
result=" "
original=word
for  i in range(len(word)-1,-1,-1):
    result=result+word[i]
if  result== original:
    print("yes")



