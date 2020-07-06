i=10
while (i>=1):
    if i==6:
        break
    print('while print: ' ,i) #1,3 --10,8
    i-=2
    print("after decr: " , i) #2,4 --8,6
print("print the last value of i: ",i)#5 --6

print()
# in while loop 'break' & 'continue' will work same
i=10
while(i>=1):
    if(i==6):
        print('if "i": ',i)#3  6
        break
    print('while "i": ',i)#1,2     10,8
    i-=2
print("outside of while loop i: " ,i)#4  


print()

i=10
while(i>=1):
    if(i==6):
        #print(i)
        continue     
    print('while "i": ',i)#1,2     10,8
    i-=2
print("outside of while loop i: " ,i)

