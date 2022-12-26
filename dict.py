d={'A':10,'B':24,'C':17,'D':40}
print(d.items())
for X,Y in d.items():
    print('key',X)
    print('value',Y)
    #bill print
menu={'rice':122,'burger':200,'dosa':120,'roti':222,'cheese chili':150,'eggs':10}
total=0
for x in menu.values():
    total=total+x
print('Bill Slip')
for a,b in menu.items():
    print(a,':',b)
print('Total Bill=',total)
