r= float(input('Enter the radius='))
h=float(input('Enter the height='))
area=3.14*(r**2)*h
print("Area of cylinder=" ,area)

a=int(input('Enter a number='))
last=a%10
L=len(str(a))
print("Length=" ,L)
first=a//(10**(L-1))
print('first=',first)
print('last=',last)

