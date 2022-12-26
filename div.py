'''dc=0
n=int(input('Enter the value of n='))
for a in range(1,n+1):
    if n%a==0:
        dc=dc+1
if dc==2:
     print(n,'is prime number=')
else:
     print(n,'is not prime number')'''
a= int(input('Enter the first number'))
b=int(input('enter rhe second number'))

while a!=b:
if a>b:
a=a-b
else:
    b=b-a
    HCF=a
print('HCF=',HCF)
