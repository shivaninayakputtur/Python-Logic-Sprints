word="hello"
reverse=[]
for char in word:
    if char in "aeiou":
        reverse.append(char)
        reverse=reverse[::-1]
print(reverse)