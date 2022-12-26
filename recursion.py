'''Recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
x=int(input("Enter a number="))
p=factorial(x)
print('Factorial of',x,'is=',p)





def sum(n):
    if n==0 :
        return 0
    else:
        return n+sum(n-1)
x=int(input("Enter a number="))
p=sum(x)
print('Total sum',x,'is=',p)'''
def sum(n):
    s=0
    while n>0:
        rem=n%10
        s=s+rem
        n=n//10
    return s
n=int(input("Enter the number="))
p=sum(n)
print("The number is ",p)
'''s=0
def sum(n):
    global s
    if n!=0:
        r=n%10
        s=s+r
        n=n//10
        sum(n)
    return s
reg=int(input("Enter the number="))
p=sum(reg)
print("sum=",p)'''

      
