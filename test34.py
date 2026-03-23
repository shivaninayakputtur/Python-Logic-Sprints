word="I love programming every day"
word1=word.split()
max_length=0
max_word2=" "
for char in word1:
    if len(char)>max_length:
        max_length=len(char)
        max_word2=char
print(max_word2)
