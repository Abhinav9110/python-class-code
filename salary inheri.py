#writw a program in python use this tocreate classs bonu containing the constructer
#defined to calculate the bonus as per detail
class Employee:  #class name
    def __init__(self,n,a,i,d): #constructor: this will automatically execute
        self.name=n
        self.age=a
        self.id=i
        self.dept=d
class Account(Employee):
    def get(self):
        self.account=345271
        self.sal=200
class Bonus:
    def __init__(self,n,a,i,d):
        Employee.__init__(self,n,a,i,d)
        Account.get(self)
        if self.sal >21600:
            self.bonus=0
        elif self.sal <=1000:
            self.bonus=self.sal*0.10
        else:
            self.bonus=5000
    def display(self):
        print('Name-',self.name)
        print("Age=",self.age)
        print('ID=',self.id)
        print("sal=",self.sal)
        print('Bonus=',self.bonus)
        print("Department=",self.dept)
obj=Bonus("Abhinav kumar yadav",35,200,"Software Engineering")
obj.display()
    
    
