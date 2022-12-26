"""exception are raised when the program is syntacikally correct  but code resultant
is correct
 try and except statememt that raised the exception are raised """
"""try:
    a=int(input("Enter a value="))
    b=int(input("Enter another value="))
    x=a/b
    print(x)
except ZeroDivisionError:
    print("cant Divide by zero")
l=[1,2,3,4,5]
try:
    print("New element is ",l[3])
    print("next element",l[5])
except:
    print('next element not present')"""
"""def fun(n):
    if n<4:
        x=n/n-1
    print(x)
try:
    fun(2)
    fun(4)
except ZeroDivisionError:
    print("can divide by zero")
except NameError:
    print("variable not defined")"""

try:
    a=int(input("Enter the value of a="))
    b=int(input("Enter the value of b="))
    c=a/b
except ZeroDivisionError:
    print("cant divide by zero")
else:
    print("Value of c=",c)
finally:
    print("End the program")






















