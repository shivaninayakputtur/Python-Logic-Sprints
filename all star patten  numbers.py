# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()
# #
# for i in range(6,0,-1):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()
# #
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()
# #
# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()
# #hollow
# a=int(input("enter a value"))
# b=int(input("enter a value"))
# for i in range(a,b):
#     for j in range(a,b):
#         if i==1 or i==4 or j==1 or j==4:
#             print("*",end=" ")
#         else:
#             print("",end=" ")
#     print()
# #
for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    for k in range(i-1):
        print("*",end=" ")
    print()

