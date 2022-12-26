#nested dictionaries
fruit={'color':{'apple':'red'},'shape':{'ciecle':'orange'}}
print(fruit['color']['apple'])
student={'name':{'Fn':'Amit','LN':'Kumar'},'DOB':{'DD':29,'MM':12,'YYY':200},'ADD':
        {'city':'jal','state':'pun','dist':'Jal'}}
#keys of the dictionaries are case sensetive
print(student['ADD']['state'])
#DICTIONARIES METHOD
#keys()
player={'name':'Abhinav','age':30,'team':'abc','role':'pqr','country':'xyz'}
print(player.keys())
print(player.values())#values
#items
print(player.items())
#update:insert the new key values pair
print(player.update({'jursey':99}))
print(player)
#get method
print(player.get('age'))
#pop :it remove the element with specified keys
player.popitem()
print(player)
#set default method
player.setdefault('country','lmn')
print(player)
player.clear
#fromkeys:return the dictionaries with speciied keys and values
d={}
t=('a','b','c','d','e')
x=10
d=dict.fromkeys(t,x)
print(d)
d={}
t=('a','b','c','d','e')
x=(10,20,30,40,50)
z=zip(t,x)
for a,b in z:
    d.update({a:b})
print(d)
t=('a','b','c','d','e','f')
l=(1,2,3)
m=(10.9,4.6,2.8)
z=zip(t,l,m)
n=list(z)
print(n)














