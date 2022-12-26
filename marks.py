reg=int(input("Enter the registration no="))
ccode=input("Enter course code= ")
tmarks=0
mte=int(input("Enter mte marks="))
tmarks=tmarks+(mte//2)
ld=int(input("Enter the number of classes delivered="))
la=int(input("Enter the number of lecture attendance="))
atp=(la/ld)*100
atp=int(atp)
print("Current attendance percentage=",atp)
if atp>=90:
    tmarks=tmarks+5
elif atp>=84 and atp<=89:
    tmarks=tmarks+4
elif atp>=80 and atp<=83:
    tmarks=tmarks+3
elif atp>=75 and atp<=79:
    tmarks=tmarks+2
else:
    tmarks=tmarks+0
ca1=int(input("Enter the marks of CA1="))
ca2=int(input("Enter the marks of CA2="))
ca3=int(input("Enter the marks of CA3="))
b1=0
b2=0
if ca1>ca2:
    b1=cal
else:
    t=ca1
    ca1=ca2
    ca2=t
    b1=ca1
if ca2>ca3:
    b2=ca2
else:
    b2=ca3
cam=((b1+b2)/60)*25
import math as m
cam=int(m.ceil(cam))
cam=int(cam)
tmarks=tmarks+cam
ete=int(input("Enter the marks of end term="))
tmarks=tmarks+ete
if tmarks>=95:
    print('O grade')
elif tmarks>=90 and tmarks<=94:
    print('A+ GRADE')
elif tmarks>=80 and tmarks<=89:
    print('a GRADE')
elif tmarks>=70 and tmarks<=79:
    print('b GRADE')
elif tmarks>=60 and tmarks<=59:
    print('c GRADE')
elif tmarks>=50 and tmarks<=49:
    print('d GRADE')
else:
    print('E_ grage')



















    












    
