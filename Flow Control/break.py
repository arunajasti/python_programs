list1 = [1,2,3,4,5,6,7]
for i in list1:
    print(i)
    if(i==4):
        break

print()
list1 = [1,2,3,4,5,6,7]
for i in list1:
    if(i==4):
        print(i)
        break

print()
list1 = [1,2,3,4,5,6,7]
for i in list1:
    if(i==4):
        print('if: ', i)
        break
    print('for: ', i)#'forloop'print after break satify this will not print
print("the outside of for loop",i)


string='aruna'
for i in string:
    if i=='u':
        break
    print('for:' ,i)#this for loop print will not execute after break satisfy
    
else:
        print(" else part will not execute")

print('aruna')

