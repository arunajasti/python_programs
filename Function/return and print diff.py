print("  #print  ")
def var():
    for x in range(2,5):
        y=x**2
        print(y)#print
    #return y it shows last value of forloop because its outside of loop.when it is List it shows all values in List check normal&ListComprehension
var() #you don't use print(var()) because you use 'print' in func

print("   #return  ")
def var():
    for x in range(2,5):
        y=x**2
        return y #return
    #return y it shows last value of forloop
print(var())


#List
print()
def var1():
    List1 = [] #empty list add values into list1
    for x in range(2,5):
        y=x**2
        List1.append(y)
        #print(List1)  #return stmt here it shows only 1st value in List1 and call the func in 'print(var1())'
    print(List1)
var1()
    
