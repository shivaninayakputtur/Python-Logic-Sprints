#square star pattern 
for i in range(6):
    for j in range(6):#diffrnce is here u gave the value toprint 6 times each line 
        print("*",end=" ")
    print("")
#increasing star pattern
for i in range(1,6):
    for j in range(i):#here it like u have to print values based on i
        print("*",end="")
    print("")
#decreasing star pattern
for i in range(6,0,-1):
    for j in range(i):
        print("*",end="")
    print()
#increasing pattern in numbers
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print("")
#same numbers in a row
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print("")
#reverse numbers in rows
for i in range(6,0,-1):
    for j in range(i):
        print(i,end="")
    print()
#pyramid with spaces
for i in range(1,6):#row
    for j in range(5-i):#space
        print(" ",end="")
    for k in range(2*i-1):#star 
        print("*",end="")
    print()
for i in range(5,0,-1):#row
    for j in range(5-i):#space
        print(" ",end="")
    for k in range(2*i-1):#star 
        print("*",end="")
    print()
#floyds triangle
num=1
for i in range(1,6):
    for j in range(i):
        print(num,end="")
        num=num+1
    print()