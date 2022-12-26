a=int(input("Enter a odd="))
b=int(input("Enter a even="))
for x in range (a,b+1,2):
   f=1
   for a in range (1,1+x):
       f=f*a
       print("factorial of ",x,"is",f)
for x in range (a-1,b+1,2):
     f=1
     for a in range (1,x+1):
         f=f*a
         print("Factorial of",x,"is=",f)
