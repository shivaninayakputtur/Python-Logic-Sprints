word="programming"
d={}
for char in word:
    if char in d:
        d[char]=d[char]+1
    else:
        d[char]=1
print(d)
max_count=0
max_char=" "
for char in d:
    if d[char]>max_count:
        max_count=d[char]
        max_char=char
second_count=0
second_char=" "
for char in d:
    if d[char]>second_count and d[char]<max_count:
        second_count=d[char]
        second_char=char

print(second_char,"appers",second_count,"times")