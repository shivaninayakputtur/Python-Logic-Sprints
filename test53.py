# function that takes list of words but return words greater thn 4
def larger(word):
    result=[]
    for char in word:# here char is word like i then love 
        if len(char)>4:
            result.append(char)
    return result
print(larger(["i", "love", "programming", "language"]))
