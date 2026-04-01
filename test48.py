#functions
def greet(name):
    print("Hello", name)

greet("Shivani")
greet("nayak")
greet("FAANG")

#1.to add 2 numbers using function

def add(a,b):
    print(a+b)
add(4.6,1)

#2.problem to find factorial value

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(5))

#3.to count vowels and consonents

def vowels(n):
    count=0
    for words in n:
        if words in "aeiou":
            count=count+1
    return count
print(vowels("shivani"))

#4.to check palindrome for numbers

def palindrome(n):
    rev=0
    original=n
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if rev==original:
        return 1
    else:
        return 0
print(palindrome(121))

# to return value of sum
def add(a,b):
    return a+b
result=add(6,10)
print(result)

            





