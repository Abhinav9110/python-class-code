"""f=open('demo.txt','r')
l=1
for x in f.readline():
    c=0
    print("Length of character",l,"=",len(x))
    l+=1"""
    
#strings are palindrom are not
old=input("Enter the string=")
new=''
l=len(old)
for x in range (l-1,-1,-1):
    new=new+old[x]
if old==new:
    print("Palindrom")
else:
    print("not palindrom")

#you have the no of alphabet starting with letter A
#extracting
