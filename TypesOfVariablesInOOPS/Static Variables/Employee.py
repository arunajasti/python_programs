#we can Access static variables by using className or obj ref
class Employee:

    company = 'Amazon' #static/class variables

    def __init__(self,name,address):
        
        self.name = name
        self.address = address

    def showDetails(self):
        print("Emp details: ",Employee.company,self.name,self.address)
        #access static variables inside method using ClassName 

e1 = Employee('aru','USA')
e2 = Employee('san','UK')

e1.showDetails()
e2.showDetails()

#print(Employee.company) or
print(e1.company) #accesing the static variables outside class by using ref or className

