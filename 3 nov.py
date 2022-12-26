"""practice pattern function"""
''''LAMBDA
USER DSEFINED
  VOID
 FRUITFUL
 BUILT IN
 ANONAYMS FUNCTION IS CREATED BY LAMDA FUNCTION WHICH TAKES N NUMBER OF ARGUMENTS BUT IT CAN HAVE ONLY ONE EXPREESSION
 SYNTEX:
     X=lamda:EXPRESSION

    # ADD 10 TO ARGUMEN A AND RETURN RESULT
x=lambda a :a+10
print(x(5))

#multiply a and b and return the result
x=lambda a,b:a*b
print(x(10,20))


#THE POWER  OF LAMBDA FUCTION IS BETER IN WHEN YOU USE ANANNYMUS FUNCTION INSIDE ANOTHER FUNCTION
def user(n):
    return lambda a:a*n
x=user(2)
print(x(3))'''


# write a function to create area of a circle
area=lambda r:3.14*r**2
print(area(3.5))
rad=float(input("enter radiud:"))
print("area of radius:",area(rad))
# x=lambda arguments: argument if cond else argument
MAX=lambda x,y,z:x if x<y and x>z else y if y>z else z
a=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))

print("Maximum value=",MAX(a,b,c))"""

