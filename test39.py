word1=input("enter the sentence:")
word2=input("enter the sentence:")
# if word2 in word1+word1:
#     print("yes rotation")
# else:
#     print("not srry ")
#rotation of letters in word
#but if length are different
if len(word1)!=len(word2):
    print("this is not possible srry")
elif word2  in word1+word2:
    print("yes rotation")
else:
    print("srry not possible maa")