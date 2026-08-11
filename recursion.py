#recursion used for  countdown
def countdown(n):
    if n==0:
        print("DONE")
        return
    print(n)
    countdown(n-1)
n=int(input("enter the value:"))
countdown(n)

#sum  of n numbers using recursion
def sum_recursive(n):
    if n==0:
        return 1
    return n+sum_recursive(n-1)
print(sum_recursive(3))

#facrorial
def factorial(n):
    fact=1
    if n==1:
        return fact*n
    return n*factorial(n-1)
print(factorial(5))

#fibonnacci
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))