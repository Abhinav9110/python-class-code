l=[[10,20,30,40],[100,200,300,400,],[5,15,25,35],[3,9,18,27]]
for a in range(len(l)):
    total=0
    for b in range(len(l[a])):
      total=total+l[a][b]
print("sum of",a+1,"row=",total)
#column
for b in range(len(l)):
    total=0
    for a in range(len(l[a])):
      total=total+l[a][b]
print("sum of",a+1,"column=",total)   
#diagonal
l=[[10,20,30,40],[100,200,300,400,],[5,15,25,35],[3,9,18,27]]
total=0
for a in range(len(l)):
    for b in range(len(l[a])):
        if a==b:
            total=total+l[a][b]
print("total sum of diagonal=",total)
#reverse diagonal
l=[[10,20,30,40],[100,200,300,400,],[5,15,25,35],[3,9,18,27]]
total=0
for a in range(len(l)):
    for b in range(len(l[a])):
        if a+b==3:
            total=total+l[a][b]
print("total sum of diagonal=",total)
