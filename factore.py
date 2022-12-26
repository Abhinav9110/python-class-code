n=int(input('Enter the value of n='))
s=0
for a in range(1,n):
    ifn%a==0:
        s=s+a
if s ==n:
    print(n,'is a perfect nmber')
else:
    print(n,'is not a perfect number=')
