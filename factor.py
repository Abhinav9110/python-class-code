"""n=int(input('Enter the value of n='))
s=0
for a in range(1,n):
    if n%a==0:
      s=s+a
if s ==n:
    print(n,'is a perfect nmber')
else:
    print(n,'is not a perfect number=')"""

n=int(input("Enter the value of n="))
e=int(input("Entr exponent value="))
P=1
for a in range(1,e+1):
    P=P*n
    print("Product is =",P)

a="A"
ord(a)
