class Employee1:

     company = 'Amazon'   #declare static variable outside method/constructor

     def __init__(self,name):
         self.name = name
         
         Employee1.empLocation = 'DENMARK'# declare static variable inside constructor using className

     def showDetails(self):
         Employee1.salary = 10000  #declare static variable inside Instance Method using className

     @classmethod
     def companyLocation(cls):
         Employee1.comLocation = 'USA'#declare static variable inside @classmethod using className or cls
         print("call static variables in classmethod by using cls or className:",cls.company)
         #or
         #cls.comLocation = 'USA'

     @staticmethod
     def employeeId():

         Employee1.empId = 3003  #declare static variable inside @staticmethod using className

e1 = Employee1('aruna')
print(e1.__dict__)

print("call static variables outside class using className or obj reference:",Employee1.empLocation)

print()
Employee1.companyLocation()  #calling class method
Employee1.employeeId()       #calling static method


e1.showDetails()
print(Employee1.__dict__) #using Employee1(className) to retrive static varibales

print()
print("call static variables outside class using className or obj reference:",Employee1.salary)

print()

e1.companyLocation()
e1.employeeId()
print(Employee1.__dict__)
