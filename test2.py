a=int(input("enter ur age"))#if elif prblms
print("ur age is",a)
if a>18:
     print("u can drive")
else:
     print("u cant drive")
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)
appleprice=100
budget=95
if appleprice>=budget:
     print("no dont buy")
else:
     print("u can buy")
num=int(input("enter the value"))
if num<0:
     print("negative")
elif num==0:
     print("zero")
elif num==99:
     print("special")
else:
     print("finally done")
#nested prblms
num=17
if num<0:
     print("negative")
elif num>0:
     if num<10:
          print("number is btw 1-10")
     elif num>10 and num<=20:
          print("number is betwwen 1-20")
     else:
          print("number is  > 20")
else:
     print("number is zero")