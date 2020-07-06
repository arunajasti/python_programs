#Multiple Inheritance: class Two is subclass of class One & class Three subclass of class Two


class One():
    def greetings(self):
        print("Welcome to classes..")

class Two(One):
    def studentInfo(self):
        print("Student Info..")
        
class Three(Two):
    def coursesInfo(self):
        print("Courses Info..")

s3 = Three()

s3.greetings()
s3.studentInfo()
s3.coursesInfo()
        
    
