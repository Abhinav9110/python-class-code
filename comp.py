    

'''age =int(input('Enter the age of voter='))
if  age >= 18:
     gender=input('Enter the gender of voter=')
     gender=gender.upper()
     if gender=='M' or gender=='MALE':
         print('Allowed the voter to vote from room no =20')
     else:
         print('Allowe the voter to vote from room no =30')
else:
         print('voter not allowed')


         M=input('enter your mobile no=')
         
         if M.isdigit()==True:
             L=len(M)
             if L==10:
                 print(M,'is valid mobile no')
             else:
                      print(M,'must contain 10 digit only')
         else:
            print('Mobile number should contain digit only')

a=int(input('enter the numberof a='))
b=int(input('enter the numberof b='))
c=int(input('enter the numberof c='))
d=(b*b)-(4*a*c)
if d>0:
   print('roots are real ')
elif d==0:
      print('roots are real and equal')
else:
    print('roots are not real')'''
'''for a in range(1,11):
    print("KOC03")
for b in range(10):
   print("KOC03",end="")
for c in range (1,5):
 print(c)'''
'''L=[1,2,3,4,5]
for a in L:
    print("hi")
for x in L:
    print("hello")
    T=(1,"A",'apple',10.6)
for a in T:
    print("INDIA")'''

#1+2+3+4+5+6+7+8+9+10
total=0
for a in range (1,11):
    total=0+2
    print('sum=',total)
    print()
N=int(input('enter the last no of series='))
even=0
odd=0
for a in  range(1,N+1):
     if a%2==0:
         even =even+a
else:odd=odd+a
print('even sum=',even)
print('odd sum=',odd)
     
   
    
