n=int(input("Enter the value: "))
for i in range(n):
    for j in range(5,7):
        print( j,end='') #this print is inside 'forloop'
                         #print(i,",",j)#if you want print i and j valuesS
    print()              #this print is for outside 'forloop'
                         #empty print() goes nextline

    
print("print the last value of i: ",i)#this print is print the 'i' last value



#another program
print()
n=int(input("Enter the num: ")) 
for i in range(n):     #rows
    for j in range(2): #cols
        #print('* ',end='')
        print(j,end="")
    print()
    

'''   
Enter the value: 4
56
56
56
56
print the last value of i:  3

Enter the num: 3
01
01
01 '''
