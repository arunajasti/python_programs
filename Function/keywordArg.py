def outer(a,b):
    add=a+b
    return a,b
#print(outer(a=2,3))   #(keyword,positional)  wrong
#print(outer(3,a=2))   # a=3,a=2 a is getting multiple arguments wrong
print(outer(2,3))      #positional arguments
print(outer(b=10,a=20)) #keyword argument
print(outer(2,b=15))    #(positional,keyword)
