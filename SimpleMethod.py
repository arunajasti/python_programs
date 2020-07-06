def add():
    a=10
    b=10 
    return a+b #return
print(add())

#or

def multiply(x,y):      
    print("multiplication",x*y)#print
    
multiply(2,4) #no need to put multiply() in 'print'         



'''when you use 'return' stmt in func
you need to call that func in 'print' stmt
print(add())

when you use 'print'stmt in func
you dont need to call that in 'print'
just call add()
 '''
import keyword
print(keyword.kwlist)
