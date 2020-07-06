def add(a,b):
    return a+b
     
res=add(2,3)   #calling function
print("addition: ",res)
#or
print("ADD:",add(2,3))  

#or
print()
def operations(a,b):
    add = a+b;
    mul = a*b;
    div =a/b;
    return add,mul #o/p will get in tuple format
    return div     #this will not work because single 'return' will works not multiples

res1 = operations(4,5)#you can call functions many times
res2 = operations(10,5)
print("opeartion1 : " ,res1)
print("opeartion2 : " ,res2)

#o/p
#opeartion1 :  (9, 20, 0.8)
#opeartion2 :  (15, 50, 2.0)
