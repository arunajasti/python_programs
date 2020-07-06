#extend() add list2 into list1
print("        Extend()")
List1 = ['sun',1,'mon',2,18.9,'sun']
print("List1 items: ",List1)
print("id: ",id(List1))
print("Lenght of list1: ", len(List1))


List2 = ['tue',3,'wed',4]  #List1.extend(['tue',3,'wed',4]) instead of creating List2
print("List2 items: ",List2)
print("Length of List2: ", len(List2))

List1.extend(List2)

print("Print list1 & list2 items using Extend(): ",List1)
print("id: ", id(List1))
print("Total Length : ", len(List1))

print('\n')

#append() it will take only one argument
print("       Append(single argument)")
List3 = ['sun',1,'mon',2,'tue',3,'wed',4]
print("Before 'thu' added into List3: " ,List3)
print("Before 'thu' the lenght is: ",len(List3))

List3.append('thu')

       #List3.append(5,'fri') it wil take only single argument
print("Print list3 add the item 'thu' using Append() : ",List3)
print("After 'thu' the length is: ",len(List3))
print('\n')
#insert the value using index
print("       Insert()")
List4 = ['sun',1,'mon',2,'tue',3,'wed',4]

List4.insert(5,'sat')

print("Insert the value using Insert(5,sat): ",List4)
print("\n")
# remove the item using item name
print("       remove(item name)")
List4.remove('sun')
print("Remove the item name using Remove(sun): ", List4)
print("\n")

#pop() it removes last item in list default
#print(List4.pop()) or it shows what item is removed

print("       Pop()")
List4.pop()
print("it removes last item in list Using pop(): ", List4) # it shows the entire list with out last item
print("\n")

#pop(i) it removes index of 2 item
print("       Pop(i)")
List4.pop(2)
print("remove the index of 2 from list Using Pop(2): " , List4)


#index(element) returns the index number
print("      Index(element)")
List5 = ["apple",'cherry','pears','banana','apple','pears']
print("returns the index of value index(2): ",List5.index('cherry') )
print("\n")

#index(ele,start,end)
print("     Index(ele,start,end)")
print("find the index of pears on/after index('pears',4,6) : ",List5.index('pears',4,6))

#count is how many times occurrence in list

print("     Count(item name)")
print("how many times PEARS are there in list: " , List5.count('pears'))
print("\n")

#sort()
print("      Sort()")
List5.sort()
print("Sort the order of List5: ", List5)

#reverse()
print("      reverse()")
List5.reverse()
print("Reverse the order of List5: ", List5)
print("\n")

#copy()
print("     copy()")
b= List5.copy()
print("copy List5 elements into b: ", b)
b[1]='mango'
print("change the index 1 value into 'mango' in b: " , b)
print("\n")
#clear
print("     clear()")
List = [1,2,3,41,2,3,5]
List.clear()
print("clear the list using Clear(): " ,List)

