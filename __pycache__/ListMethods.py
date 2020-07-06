 # List Methods
           #extend
 
 #list1.extend(list2)  i.e., means adding list2 into list1

list1 = ['aruna',1.45,9,'c',999]
print("Before update: ",list1)

list2 = ['bolla','latha']

list1.extend(list2) # gropu of elments added

print("After Updated List using extend(): ",list1)
print(len(list1))

list1.extend('sandhya')
print(list1)

#list3 = list1.extend(list2) # this 2 stmts will not work we dont assign extend to another variable
#print(list3)

 #append() always single argument take abd add to list at end

list1.append('rani')
print(list1)

list3 = ['aruna',1.45,9,'c',999,'b']

list4 = ['bolla','latha'] # if 2 items add  in to list 3  using apppend() it will take it as single item

list3.append(list4)

print(list3)

print(len(list3))


