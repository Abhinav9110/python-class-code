#Dictname={k:v for loop in zip object}
l=['Apple','banana','Guava','orange','grapes']
c=['red','yellow','green','black','blue']
fruit={k:v for (k,v) in zip(l,c)}
print(fruit)

d={x:x**2 for  x in range(1,11)}
print(d)
