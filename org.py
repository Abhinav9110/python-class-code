"""n=int(input('Enter the number='))
org=n
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**3)
    n//10
if org==sum:
   print(org,'is armstrong number=')
else:
    print(org,'is not armstrong')"""

SUM=0
import math as m
n=int(input('enter the number='))
org=n
L=int(m.log10(n))
while n!=0:
      r=n%10
      SUM=SUM+(r**(L+1))
      n=n//10
if org==sum:
    print('Armstrong')
else:
    print('Not Armstrong')

