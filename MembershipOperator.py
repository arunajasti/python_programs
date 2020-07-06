List1 = [1,2,3,4]
List2 = [4,5,6]
for item in List1:
    if item in List2:
        print("Overlapping")
    else:
        print("not Overlapping")


#identity
print()
a=10
b=10
c= a is b
print(c)
print(id(a))
print(id(b))
