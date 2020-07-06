x=2
def foo():
    x=10
    #x=x**2 it gives error 
    print(x)                      #10
foo()
print(x)#it gives global value      2

print()

x=2
def foo():
    global x
    x=x**2 
    print("inside x: ", x)
    
print("it executes first before func: " ,x)    
foo()
print("it executes after func x: ", x)#this prints at end of the function and it gives inside func val
