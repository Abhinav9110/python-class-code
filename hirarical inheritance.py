class Value:
    def __init__(self,a,b):
        self.v1=a
        self.v2=b
class Sum(Value):
    def __init__(self,a,b):
        Value.__init__(self,a,b)
        self.c=self.v1+self.v2
    def display(self):
        print('Sum=',self.c)
class Product(Value):
    def __init__(self,a,b):
        Value.__init__(self,a,b)
        self.p=self.v1*self.v2
    def display(self):
        print("Product=",self.p)
o1=Sum(10,20)
o1.display()
o2=Product(30,20)
o2.display()
        
"""
   product
   |     |
value    sum


"""
