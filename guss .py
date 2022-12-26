#28 oct

"""import random as r
a=int(input("Enter the begeninig value ="))
b=int(input("Enter the begeninig value ="))
if a>b:
      print("Not Allowed ")
else:
    n=r.randint(a,b)
    for x in range(a,b+1):
        if n==x:
            print("Gussed number=",x)
            break"""
"""#write a program for throwing  the dice a get the number
import random as r
n=6
a=0
b=0
c=0
d=0
e=0
f=0
g=0
for x in range (n):
    num=r.randint(1,6)
    if num==1:
        a=a+1
    elif num==2:
        b=b+1
    elif num==3:
        c=c+1
    elif num==4:
        d=d+1
    elif num==5:
        e=e+1
    elif num==6:
        g=g+1
    else:
        f=f+1
print("1 comes on dice",a,"times")
print("2 comes on dice",b,"times")
print("3 comes on dice",c,"times")
print("4 comes on dice",d,"times")
print("5 comes on dice",e,"times")
print("6 comes on dice",g,"times")"""
# print  the list of prime number
def primelist(x,y):
    for a in range (x,y+1):
        dc=0
        for b in range (1,a+1):
            if a%b==0:
                dc=dc+1
        if dc==1 or dc==2:
            print(a)
p=int(input("enter a 1 number "))
q=int(input("Enter second number="))
print("list of prime number is between",p,"and",q,"are")
primelist(p,q)
'''  # compare the string              
s1=input("Enter the string1=")
s2=input("enter the string2=")
if ord(s1[0])<ord(s2[0]):
 print("first string is less than second string")
elif ord(s1[0])>ord(s2[0]):
    print ("second string is less than first than first valur")
else:
    print("Both string has equal ascii value")'''










  
