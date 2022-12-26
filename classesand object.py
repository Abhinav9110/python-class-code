#class and object
"""class player:
    def get(self):
        self.name="xyz"
        self.age=20
        self.country="India"
    def display(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("country=",self.country)
obj=player()
obj.get()
obj.display()"""
class student:
    def get(self,n,r,b):
        self.name=n
        self.reg=r
        self.branch=b
    def display(self):
        print("Name=",self.name)
        print("Reg=",self.reg)
        print("Branch=",self.branch)
o=student()
name=input("Enter student name=")
reg=int(input("Enter the registration number="))
B=input("Enter the branch=")
o.student(name,reg,B)
o.display()
x=student()
x.get(name,reg,B)#("abc",123,"CSE")
x.display()
#data abstration














