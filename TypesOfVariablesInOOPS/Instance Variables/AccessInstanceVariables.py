#How to access Instance Variables inside method & outside class

class AcessInstanceVariables:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def info(self): #this is instance method why because using 'self' as argument
        print("Accessing Instance Variables in Method By Using self")
        print(f'Student name & rollno {self.name},{self.rollno}')

s1 = AcessInstanceVariables('aru',101)
s1.info()


print('Accessing instance variables from outside of class using reference s1')
print(s1.name,s1.rollno)

