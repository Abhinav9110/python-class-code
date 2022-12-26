"""create a class in python having name user contaninig a method get details of the user like username,address,mobile,
create another calass having name company containing contanong
one method detain defining to get the company details such as
name ,details ,turn over use both class to create the class
emplyee,performerece this cals is cintaining  ne constructer
used to inililize the parameter grade and one method display"""
#multiple inheritance
class User:
    def get(self):
        self.name=input("Enter name=")
        self.age=int(input('Enter age='))
        self.add=input("Enter address=")
        self.mob=input("Enter mobile=")
class Company:
    def getdetails(self):
        self.cname=input("Enter company name=")
        self.noe=int(input("Enter number of employee="))
        self.cadd=input("Enter company add=")
class Performance(User,Company):
    def __init__(self,g):
        self.grade=g
    def display(self):
        User.get(self)
        Company.getdetails(self)
        print('Name=',self.name)
        print('age=',self.age)
        print('Adress=',self.add)
        print('grade=',self.grade)
        if self.grade=='O':
            print('Outstanding')
        elif self.grade=='A':
            print("Excellent")
        else:
            print("Poor")
G=input("Enter grade value=")
G=G.upper()
if len(G)==1:
  obj=Performance(G)
  obj.display()
