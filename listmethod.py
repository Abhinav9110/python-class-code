l=[]
#append :it add element to last
#list.append(element)
l.append(10)
print(l)
#insert()
#list.insert(index,element)
l.insert(0,40)
print(l)
#remove :it remove the element from list
m=[1,2,3,4,5,6,7,8]
m.remove(4)
print(m)
#pop: it remove the element from the last
m.pop()
print(m)
m.pop(1)
print(m)
"""#del
x=['a','b','c']

del(y[0])
print(y)"""
w=[1,23,45,67,89,50,89,50,50,50]
#index()
i=w.index(50)
print(i)
#count:it counts the element
c=w.count(50)
print(c)
#reverse()
w.reverse()
print(w)
#sort: it sort the element into acending order
l1=[1,324,567,98,57,8,4,7,36,36,64,2,34,5,7,8,9,0,1,2,3,5]
l2=[4,45,67,89,87,65,67,6]
l1.sort(reverse=True)

print(l1)
#extent:
l1.extend(l2)
print(l1)
#clear():it will clear the element
#build the loist at n time
l=list()
n=int(input("Enter size of list="))
for x in range(n):
    e=int(input("Enter element="))
    l.append(e)
    print("created list")
    print(l)

#derive an logic 






