print("Normal func")
def var(a):
    List1 = []
    for x in a:
        List1.append(x)
        #print(List1)   # return List1 it shows single value because its inside for loop
    print(List1)        # return List1 it shows all because its outside for loop and it List.if itis not list it shows last value  
var('aruna')

print(" List Comprehension ")

var = [x for x in 'aruna']
print(var)
