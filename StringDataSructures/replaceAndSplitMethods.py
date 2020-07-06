string = "Aruna, is a goog girl & Aruna, is a nice"

#replace Method
b = string.replace("Aruna" ,"Sandhya")#old,new
print(b)

# or print(string.replace("Aruna", "sandhya") instead of 2 lines you can write in single line

#i want replace sandhya with 1st place

print(string.replace("Aruna","Sandhya",1))#old,new,count
      
#split Method

print("Using split method: ", string.split())#split by each word in form of list

print("Length of String: ",  len(string))

#Now print the length of split string
print("Length of split() string:", len(string.split()))

#argument in split
print("Argument in split():" , string.split(',') , len(string.split(',')))
