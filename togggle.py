#write a program in python to convert all the chaeacter in toggle case
f=open('abcd.txt','w')
f.write("This is class Python Programming\n")
f.write("COURSE CODE INT108\n")
f.write("section Koc03\n")
f.write("No of students=\n")
f.close()
with open("abcd.txt",'r') as ab:
    data=ab.read()
f=open('new123.txt','w')
e=''
for x in data :
    if ord(x)>=65 and ord(x)<=90:
        t=ord(x)
        t=t+32
        e=e+chr(t)
        f.write(e)
    elif ord(x)>=47 and ord(x)<=122:
        t=ord(x)
        t=t-32
        e=e+chr(t)
        f.write(e)
    else:
        e=e+x
        f.write(e)
f.close()
        
        
