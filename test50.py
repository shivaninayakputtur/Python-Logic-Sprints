def word_count(word1):
    word2=word1.split()
    count=0
    for word in word2:
        count=count+1
    return count
print(word_count("shivani is a programmer"))