a=100 #global scope
b=10
def local():
    #a=10 #local scope
    print ("a value inside func: ", a)#2nd inside print func
    print ("b value inside func: ", b)
    
print(" a value outside of func: ", a)#1 1st prints outside print func
local()
print("at end of line: " ,a)#3rd 

print()
#2nd
def local():
    a=20 #local scope
    print(" a value inside func: " ,a)#2nd

a=50#global scope
print(" a is outside func: ", a) #1st
local()

print()
#3rd
def local():
    name='aruna'
    age=34
    print("inside func: "+ name,age,place)#here place is not assign in inside func but it takes global place value

name='suni'
age=36
place='India'
print("outside func: " + name,age,place)
local()

#4th
#def local(value):
    
    
