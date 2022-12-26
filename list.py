#List is a hrtrogeneous  and is enclosed in square bracket [] and index start from 0 to n-1 ,it is mutable,
l=[1,2,3,4,5,6,7,8]
print(type(l))
print(len(l))
z=list(range(1,11))
print(z)
S="INDIA"
M=list(S)
print(M)
# Acessing the eleements of list
L=[10,20,30,30,40,50,60,70,8,91,90]
print(L[4])
print(L[7])
#update
L[5]=50000
print(L)
L[7:10]=[1000,1000,1000]
print(L)
# variou operation on the list
#1.concetination[+]:iT join ist With other list
L1=[1,3,4,6]
L2=[4,5,6,7]
L3=[7,8,9]
L=L1+L2+L3
print(L)
#Repetition[*]
m=[5,10,12,45]
mn=m*3
print(mn)
#method:max(),min(),sum()
T=[10,20,30,40,50,60,70,80,90]
print(max(T))
print(min(T))
print(sum(T))
print(sum(T)/len(T))
#list slicing
#list[start:stop:step]
A=[1,2,3,4,5,6,7,8,9,0,11,22,33,4,55,67,88,9]
A1=A[4:10:1]
print(A1)











