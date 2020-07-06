#single inheritance with constructor arguments
class Superclass():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    '''def setData(self,name,age):
        self.name=name
        self.age=age'''
        
    def superMethod(self):
        print("superclass name & age:",self.name,self.age)

class Subclass(Superclass):
    def __init__(self,name,age,department):
        super(Subclass,self).__init__(name,age)#imp accessing superclass instance variables into subclass
        #self.setData(name,age)
        self.department = department
        
    def subMethod(self):
        print("subclass department:",self.department,self.name,self.age)


s2 = Subclass('aruna',32,"IT")

#s2.superMethod()
s2.subMethod()
