class Super1():
    company = 'Amazon'
    def __init__(self,name):
        self.name = name
    def data(self):
        print("super1: ",self.name)
    @classmethod
    def classMethod(cls):
        return cls.company
    
    @staticmethod
    def showData():
       print("ShowData:" ,Super1.company)


class Super2():
    def __init__(self,name):
        self.name = name
    def data(self):
        print("super2: ",self.name)


class Sub(Super1,Super2):
    def __init__(self,name):
        self.name = name
    


    
s1 = Sub('ARUNA')
s1.data() #it prints super1 data()
print(s1.classMethod())
s1.showData()
