#strings
# name="shivani Nayak"
# print(name.upper())
# print(name.lower())
# print(name.replace("a","o"))
# print(name[0])
# print(name[-1])
# print(len(name))
#to get length of each word
# sentence="I love coding every day"
# words=sentence.split()
# print(len(words))
#same but with user input
# n=input("enter the sentence:")
# words=n.split()
# print(len(words))
#to get the number of repitative word in a given word
# word="programming"
# print(word.count("m"))
# print(word.count("g"))
# print(word.count("r"))
#it checks how many times a leeter appeard the most time not manually using dictionary
# word="Shivani Nayak"
# d={}
# for char in word:
#     if char in d:
#         d[char]=d[char]+1
#     else:
#         d[char]=1
# print(d)
# max_count=0
# max_char=" "
# for char in d:
#     if d[char]>max_count:
#         max_count=d[char]
#         max_char=char
# print(max_char,"appers",max_count,"times")
# word = input("enter word:")
# word1 = input("enter word:")
# w=sorted(word)
# w1=sorted(word1)
# if w==w1:
#     print("anaragram")
# else:
#     print("nope not")
#vowels and consonents 
word=input("enter")
count=0
count1=0
for i in range(len(word)):
    if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u":
        count=count+1
    else:
        count1=count1+1
print(count)
print(count1)
#if dont need space thn just do an elif conditionnof eliword[i]!=" "
