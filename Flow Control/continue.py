list1=[1,2,3,4,5,6,7]
for i in list1:
    if(i==4): #if condition stisfy it skipsthe value
        continue
    print('for: ' ,i)#if continue satisfy it wont print that value

print(i)

print()
list1=[1,2,3,4,5,6,7]
for i in list1:
    if(i==4): 
        continue
    print('for: ' ,i)
#print("before else") this print will not work before else
else:
    print("after CONTINUE the else part execute:")
