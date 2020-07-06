#per obj the constructor will execute only 1 time
#At the time of obj creation automatically the constructor will be executed
#method will execute many times(if you calll method 2 times,the method will execute 2 times using same obj)
class Constructor1:

    def __init__(self,name,rollno):

        self.name = name
        self.rollno = rollno
        print("Constructor will be execute")

    def info(self):
        print(self.name)

s1= Constructor1('aru',101)#consructor will execute 1 time per obj

s1.info()#calling method 2 times
s1.info()

s2= Constructor1('san',102)#another obj creation

#s3= Constructor1('sun',103)
