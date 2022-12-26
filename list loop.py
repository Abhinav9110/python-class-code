"""#ILETEATE THE FOR LOOP OVER A LIST
L=[10,20,390,40,50,60,70,80,90]
for x in L:
    print(x)
for x in range(len(L)):
    print(L[x])
l=[10,2,44,67,89,45,67,54,95,9,23,43,24,42,54,45,]
total=0
for x in l:
    total=total+x
print("total sum=",total)
l=[23,45,65,78,87,90,98,78,45,65,34,26]
result=False
s=int(input('Enter the element you want to search:'))
for x in range (len(l)):
    if s==l[x]:
        print(s,"found at index location=",x)
        result=True
        break
if result==False:
    print(s,"does not exist")
# find no times any number occor
l=[23,45,65,78,87,23,98,78,23,65,34,26]
count=0
result=False
s=int(input('Enter the element you want to search:'))
for x in range (len(l)):
    if s==l[x]:
        count=count+1
       # print(s,"found at index location=",x)
        result=True
        #break
if result==False:
    print(s,"present o times")
else:
    print(s,"present ",count,"times")



# compare min and max
l=[12,34,56,76,78,98,32,23,45,54,67,87,67]
mx=l[0]
mn=l[0]
for x in l:
    if mx<x:
        mx=x
for y in l:
    if mn>y:
        mn=y
print("maximum",mx)
print("minimum",mn)"""

#nested list :list within list is caled nested list

l=[37,56,[45,67,87,45],44,77]
print(l[2])
#list[outer index][inner index]
print(l[2][2])
l=[1,2,[3,[4,5,6],7],8,9,[10,11,[12,[13,14],15]]
print(l[2][1][1])

















    
