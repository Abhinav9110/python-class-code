"""class display:
    def __init__(self,*args):
        if len(args)==1 and type(args[0])==int:
            self.x=args[0]
            print("square=",self.x**2)
        if len(args)==1 and type(args[0])==float:
            self.r=args[0]
            print("Area of circle=",3.14*self.r**2)
        if len(args)==2 and type(args[0])==int:
            self.x=args[0]
            self.y=args[1]
            print("sum ",self.x+self.y)
obj=display(10)
obj2=display(7.7)
obj3=display(5,6)"""
# __str__ (self)
class student:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def __str__(self):
        return f"Name of company is{self.name}({self.age})"
obj=student("vi",80)
print(obj)
    
