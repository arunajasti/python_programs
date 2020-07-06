str1 = "Aruna"
print("print length of string: ", len(str1))
# i want print first 2 letters i.e., it string slicing using []


print(str1[0]) #print 1st letter of string
print(str1[0:2])#print first 2 letters 0: included 2: excluded
print(str1[1:5])
print("if starting index is high then second ", str1[4:1]) # no o/p

print(str1[-1])#-ve index reads from right to left
               # a
print("print the start using -ve index: " , str1[-5:-1]) #Arun

print("print the start using -ve index: " , str1[-1:-5]) # no o/p here
 

print(str1[1:]) #prints from 1st index to end runa
print("prints from start index before 4th index ",  str1[:4])

#[start:stop:jump]

print(str1[0:5:2])# here take first 0:5 i.e., Aruna and :2 means jump(it jumps 2 letters)
                  #Aua
print(str1[::-2]) #auA


print(" " , str1[4:0:-2])
print(str1[0:4:-2]) # no o/p because if jump is -ve index should be higher than the ending index

