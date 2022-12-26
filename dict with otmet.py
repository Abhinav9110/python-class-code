old_price={'milk':1,'breed':2,'cheese':4}
d_r=80
new_price={key:value*d_r for key,value in old_price.items()}
print(new_price)
#condition in dictionary compression
import string as s
l=list(s.ascii_uppercase)
print(l)
n=list(range(1,27))
d={k:v for k,v in zip  (l,n) if v%2==0}
d1={k:v for k,v in zip(l,n) if v%2!=0}
print(d)
print(d1)
