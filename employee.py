class Employee:
    def __init__(self,name,department):
        self.name = name
        self.department = department
        #print(self.name,self.department)
    def info(self):
        self.salary = 10000


e1 = Employee('suni','HR')

e1.info()

print(f'employee Info {e1.__dict__}')
    #or
print('employee Info',e1.__dict__)
