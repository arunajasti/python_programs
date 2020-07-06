def outer():
    a=10
    def inner():
        a=20
        print("inner() a=20: ", a)#1  20
    inner()
    print(a)#2                        10
outer() #call outer func


print()
def outer():
    a=10
    def inner():
        nonlocal a
        a=20
        print("inner() a=20: ", a)#1   20
    inner()
    print(a)#2                         20
outer() #call outer func



print()
c =1
def foo():
    nonlocal c
    c=c+2
    print(c)
foo()

