veg=['Rice','Dal','Burger','Roti','Dosa','Paneer','Soap']
vp=[100,120,60,15,60,56]
nveg=['Chicken','Egg','Fish']
np=[200,300,150]
snack=['Manchurian','Springroll','Noodles']
sp=[130,20,110]
n=int(input('Enter no of veg items='))
for a in range (len(veg)):
    veg[a]=veg[a].upper()
for b in range(len(nveg)):
    nveg[b]=nveg[b].upper()
for c in range (len(snack)):
    snack[c]=snack[c].upper
menu={}
for x in range(n):
    name=input('Enter veg dish name=')
    name=name.upper()
    quantity=int(input('Enter quantity'))
    for a in range(len(veg)):
        if veg[a]==name:
            menu.update({name:quantity*vp[a]})
p=int(input('Enter no of non veg items'))
for x in range(p):
    name=input('Enter non veg dish name=')
    name=name.upper()
    quantity=int(input('Enter quantity='))
    for a in range(len(nveg)):
        if nveg[a]==name:
            menu.update({name:quantity*np[a]})
s=int(input('Enter no of snack items='))
for x in range(s):
    name=input('Enter snack dish name=')
    name=name.upper()
    quantity=int(input('Enter quantity='))
    for a in range(len(snack)):
        if snack[a]==name:
            menu.update({name:quantity*sp[a]})
print('ordered menu')
for a,b in menu.items():
    print(a,':',b)
total=0
for x in menu.values():
    total=total+x
print('Total Bill=',total)







