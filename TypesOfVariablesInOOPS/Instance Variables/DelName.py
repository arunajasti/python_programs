#delete the instance variables

class DelName:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def info(self):
        del self.name

s1 = DelName('aru',101)
print('Before calling info()')
print(s1.__dict__,end = "\n\n")


print('After calling info()')
s1.info()
print(s1.__dict__)
