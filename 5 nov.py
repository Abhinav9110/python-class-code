"""
# write a function with variable length arguments that prints the total average of all the arguments
def my_function(*args):
  total=0
  for x in args:
      total=total+x
  avg=total/len(args)
  return avg
a=int(input("Enter first value="))
b=int(input("Enter second value="))
c=int(input("Enter third value="))
d=int(input("Enter forth value="))
A=my_function(a,b,c,d)
print("Average=",A)"""
#  write a function that accept the list of n number of arguments and returns the total count of even and odd values arguments.
L=[]
n=int(input("Enter the value of n="))
for x in range (n):
    e=int(input("enter the list element="))
    L.append(e)
def countevenodd(LIST):
    ec=0
    oc=0
    for x in LIST:
        if x % 2==0:
            ec=ec+1
        else:
            oc=oc+1
    return ec,oc
a,b=countevenodd(L)
print("Even value=",a,"oddvalue=",b)


























