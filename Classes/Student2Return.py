class Student1:
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def info(self):
        return f'student name is {self.name}' #return stmt

s1 = Student1('Ram',10,1)
s2 = Student1('Arjun',7,2)

print(s1.info())# you should use print() func to call the method
print(s2.info())
