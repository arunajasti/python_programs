#while with break

i=10
while(i>=1):
    if i==4:
        break
    print(i)
    i-=2
print("the last i iterate:",i)

#while with continue
print()
i=10
while(i>=1):
    if i==4:
        continue
    print(i)
    i-=2
print("the last i iterate:",i)#this line will not execute

#while with break & else
i=10
while(i>=1):
    if i==4:
        break
    print(i)
    i-=2
#print("the last i iterate:",i) #dont write print stmt before else with same align
else:
    print('goog')
