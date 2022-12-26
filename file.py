f=open('file.txt','w')
f.write("xyz\n")
f.write('computer science\n')
f.write('KOC03\n')
f.write('122345\n')
f.write('address\n')
f.close()
'''ord('A')=65
ord('z')=90
ord('')=97
ord('')'''
upper=0
lower=0
vowels=0
spaces=0
digits=0
others=0
with open('file.txt','r') as ab:
    data=ab.read
    newdata=data[0::1]
for x in newdata:
    print(x)
for x in newdata:
    if ord(x)>=65 and ord(x)<=90:
        upper+=1
    elif ord(x)>=97 and ord(x)<=122:
        lower+=1
    elif ord(x)>=45 and ord(x)<=57:
        digits+= 1
    elif ord(x)==32:
        spaces+=1
    else:
        others+=1
print('Upper case letters=',upper)
print('lower case letters=',lower)
print('Digits=',digits)
print('Spaces=',spaces)
print('Special character=',others)
for x in newdata:
    if x=='a' or x=='A' or x=='e' or x=='E' or x=='i' or x=='I' or x=='u' or x=='U':
      vowels+=1
print('No of vowels =',vowels)
















        
