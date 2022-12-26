
"""import random as r
# random:random function generates multiple  number between 0 to 0.1
n=r.random()
print(n)
#choice:choice is the inbuilt function that returns a random value from the list of numbers,tuple of integer
l=[25,17,91,63,44,32,5]
num=r.choice(l)
print(num)
t=(5,23,44,69,38)
s=r.choice(t)
print(s)
s="nishith"
c=r.choice(s)
print(c)
l=r.randrange(10,20)
print(l)
for x in range (2):
    print(r.randrange(10,20))
# guess the number"""
result=False
n=int(input("Enter the number"))
for x in range(1,101):
    if n==x:
        print("The number is =",x)
        result=True
        break
if result==False:
    print(n,"not found")
# wrie a progrm that generates factorial of 10
for x in range (1,11):
    f=1
    for a in range (1,1+x):
        f=f*a
        
    print("Factorial of ",x,"is",f)
