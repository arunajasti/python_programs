list1 = [1,2,3,4,5,6,1,3,4,'aruna',45.7]

print("print the all items in list: ", list1) #it prints all the items in list



print("print last item in list value list1[-1] : ",list1[-1])#print last item in list 
print("print index '0' value list[0] : ",list1[0]) #it prints '0' index item

b=list1[1]# we can write 2 lines to execute the index 1 or single line like above line
print("print Index '1': ",b)

# i want change index 4 value with latha
list1[4]='latha'
print("print after changing values: ", list1)

#Delete the element
list1.remove('aruna')
print("After remove aruna item ",list1)


list1.pop() # it remove last item default if we dont give index in argument

print("removes last item using pop(): ",list1)

c = list1.pop(4)
print("removes index 4 using pop(4): ",c)

#print(list1.count(1)) # or
b = list1.count(1)
print(b)
