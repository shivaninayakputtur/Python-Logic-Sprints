n = int(input("Enter a positive integer: "))
if n <= 0:
 print("Please enter a strictly positive integer.")
else:
 print(f"Collatz sequence for {n}:")
 print(n, end=" ") 
 while n != 1:
    if n % 2 == 0: 
        n = n // 2 
    else: 
        n = 3 * n + 1
 print(n, end=" ")