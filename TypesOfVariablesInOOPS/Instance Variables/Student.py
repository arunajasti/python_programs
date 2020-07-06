class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno    #inside Constructor using self

    def info(self):
        self.marks = 60         #inside instance method usinf self
#-------------------------No print,No return stmt
s1 = Student('aruna',1)
s2 = Student('sandhya',2)

s1.age = 10                    #outside class using reference
s2.age = 20

s1.info()
s2.info()

print('s1 Student: ' ,s1.__dict__) # print all values using dict
print('s2 Student: ' ,s2.__dict__)

s3 = Student('suni',3)
s3.dept = 'HR'
#i didnt call s3.info() so in o/p 'marks' wouldn't show
print('s3 student: ',s3.__dict__)


#s1 Student:  {'name': 'aruna', 'rollno': 1, 'age': 10, 'marks': 60}
#s2 Student:  {'name': 'sandhya', 'rollno': 2, 'age': 20, 'marks': 60}

# if i dont call s1.info() in o/p the marks wouldn't show
 
