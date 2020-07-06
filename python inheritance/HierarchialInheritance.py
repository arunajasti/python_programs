#//www.includehelp.com/python/example-of-hierarchical-inheritance-in-python.aspx
#it shows the other way how to access superclass instance variables in subclasses
    
class Details():
    def __init__(self,name,id,gender):
        self.name = name
        self.id =id
        self.gender = gender

class Employee(Details):
    def __init__(self,name,id,gender,department):
        super(Employee,self).__init__(name,id,gender)
        self.department = department
    def empData(self):
        print("Emp details: ",self.name,self.id,self.gender,self.department)

class Doctor(Details):
    def __init__(self,name,id,gender,speciality):
        super(Doctor,self).__init__(name,id,gender)
        self.speciality = speciality
    def docData(self):
        print("Doc details: ",self.name,self.id,self.gender,self.speciality)


emp = Employee('aruna',101,'F','IT')
emp.empData()
#print(emp.__dict__) i shows the o/p in dict format

doc = Doctor('sandhya',101,'F','CARDIO')
doc.docData()
