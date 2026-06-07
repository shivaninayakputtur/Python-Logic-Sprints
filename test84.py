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
