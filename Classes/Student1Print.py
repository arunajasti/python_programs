class Student:
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
        
    def info(self):
        print(f"student name is {self.name}") #print stmt
        #print(f"student name is {s1.name}")
        
        
s1 = Student('Ram',27,1)
s2 = Student('Arjun',25,2)


s1.info()#no need to use print () to call the method s1.info()
s2.info()
