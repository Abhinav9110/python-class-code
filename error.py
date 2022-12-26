import requests as rq
from bs4 import Beautifulsoap
res=rq.get('http://www.wikipedia.org')
s=Beautifulsoap(res.txt,'html.parser')
ptags=s.select("p")
f=open('web.txt','w')
for x in ptags:
    f.write(str(x.txt))
f.close()
fromgoogle.colab import files
files.download('web.txt')
