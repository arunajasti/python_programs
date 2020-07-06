List1 = ['sun','mon','tue','wed','d']
List2=[1,2,3,2,0]


x = len(List1)
print("Print the len of List1:  " ,x)# or print(len(List1))
print("order get sorted by asc: ",sorted(List1))
print("to get the max in list:  ",max(List1))
print("to get the min in list:  ",min(List1))
print("in list2 if '0' available shows: ",all(List2))
print("in list2 if '0' available shows: ",any(List2))
print("sum of two lists: ",sum(List2)) 
#print(sum(List1))#sum function will not add int & str 
