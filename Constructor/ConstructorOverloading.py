#there is no Constructor overloading concept in PYTHON
#if there morethan 1 constructor the last constructor will execute
#what evere the last constructor,create the obj that constructor

class ConstructorOverloading:

    

    def __init__(self,name):#with parameter #1
    
        print("parameter constructor")
        self.name = name
        print("parameterized constructor:" , self.name)

    def __init__(self,name,rollno):          #2
        self.name = name
        self.rollno = rollno
        print("2 parameters:",self.name,self.rollno)

    def __init__(self): #no parameter        #3
    
        print("default constructor")
        

s1 = ConstructorOverloading() #creating obj of last constructor

#s3 = ConstructorOverloading('san',102)
#s2 = ConstructorOverloading('aru')

