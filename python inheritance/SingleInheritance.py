#single Inheritance one superclass & one subclass
class Superclass():
    def superMethod(self):
        print("Superclass Method")

class Subclass(Superclass):  #in parenthesis we use superclass name
    def subMethod(self):
        print("Subclass Method")

s1 = Subclass() #create an obj of subclass so we can access superclass methods

s1.superMethod()
s1.subMethod()


