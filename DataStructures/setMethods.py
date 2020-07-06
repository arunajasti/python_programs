print("  set Methods  ")

print("   ##### add() ##### ")
print("\n")
set1 = {'aru',2,'sun',99.9,'san'}      
set1.add("bolla")
print("print the values after add the 'bolla' item into set1: ",set1)

print("\n")
print("    ##### update() ##### ")
ab = {2,3,4}
bc = {56,7,1}
ab.update(bc)
print("print add the 'bc' set into existing 'ab' set using update(): ",ab)
print("\n")
#union() means or

set2 ={'latha',29+7j,'aru','san'}
c = set1.union(set2)      
print("print set1 & set2 using union(): " , c)

#intersection means matching elements
d= set1.intersection(set2)
print("print matching elements using intersection(): " ,d)

#difference  
e= set1.difference(set2) #print set1 elements ummatched of set2
print("print unmatched elements of set1 using difference(): " ,e)

f=set2.difference(set1)  #print set2 elements unmatched of set1
print("unmatched elements of set2 using difference(): " ,f)

#pop()
print("showing which element removed: ",set1.pop())
print("remove last item of set1 using pop(): " ,set1)

#issuperset
set3={1,2,3,4,5,'san'}
set4={2,3,4}

print(set3.issuperset(set4))  #True
print(set4.issuperset(set3))  #False
print(set3.issubset(set4))    #False
print(set4.issubset(set3))    #True

#clear()
set4.clear()
print("clear set4: ", set4)
