""" nested for
for x in range(1,11):
    for y in range (1,11):
       print(x,'*',y,'=',x*y)
  
 n=int(input('Enter the number='))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
 78
 print('reverse=',rev)
n= int(input('enter the number='))
m=n
rev=0
while n>0:
     r=n%10
     rev=rev*10+r
     n=n//10
     print('reverse=',rev)
     if m==rev:
        print(m,'is panlindrome')
     else:
        print(m,'is not palindrone')
n= int(input('Enter the number='))
s=0
while n!=0:
    r=n%10
    s=s+r
    n=n//10
print('Total sum=',s) """
n=int(input('Enter ther number='))
ec=0
oc=0
zc=0
while n!=0:
    r=n%10
    if r==0:
        z=zc+1
    elif r%2==0:
        ec=ec+1
    else:
        oc=oc+1
    n=n//10
print('Total Even=',ec)
print('Total odd=',oc)
print('Total zero=',zc)

        
