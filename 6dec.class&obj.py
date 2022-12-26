class calculate:
    def area(self,*args):
        if len(args)==1:
            self.side=args[0]
            print("Area of square=",self.side*self.side)
        if len(args)==2:
            self.l=args[0]
            self.b=args[1]
            print("Area of rectangle=",self.l*self.b)
        if len(args)==3:
            self.l=args[0]
            self.b=args[1]
            self.h=args[2]
            print("Volume of cuboid=",self.l*self.b*self.h)
"""a=calculate()
a.area(10)
a.area(10,20)
a.area(10,20,30)"""
n=int(input("Enter your choice="))
if n==1:
    x=int(input("Enter the side of square"))
    obj=calculate()
    obj.area(x)
if n==2:
    x=int(input("Enter lemgth="))
    y=int(input("Enter breath="))
    obj=calculate()
    obj.area(x,y)
if n==3:
    x=int(input("Enter lemgth="))
    y=int(input("Enter breath="))
    z=int(input("Enter height"))
    obj=calculate()
    obj.volume(x,y,z)
    
