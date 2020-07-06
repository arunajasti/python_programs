#for 1
for x in ('apple',2,3,4,1):
    print(x)
    
#for 2
print("#####  for #####")
string='apple'
for x in string:
    print(x)
    
#for 3
print("#####  for #####")
string='apple'
for x in string:
    print(string)
    print(x) #this print is still in loop #difference is Indentation
    
print("its print last item i.e., : ",x) #this print is outside of for loop & prints last item 
    
    
#range
print("#####  range() #####")

for y in range(1,5):
    print(y)


#list
print("#####  'list1' #####")

List1=['apple','banana','cherry']
for x in List1: 
    print(x)
    
  
print("#####  'list2' #####")

List2=['apple','banana','cherry']
for x in range(len(List2)): #len(List1) is '3' so range(3)
    print(List2[x])#here retrieve the values using index
    
#dict
print("#####  'dict' #####")

var ={'name': 'aruna','age':32,'height':5.4}
for x in var: #var it send keys to 'x'
    print(x)#the 'x' prints the keys

print("\n")
for x in var.items():  #var.items() is print all keys & values
    print(x)

print("\n")
for x in var.values():#var.values prints only values
    print(x)

#you can use "var.get(x)" to print keys & values instead of "var.items()" 
print("\n")
for x in var:
    print(x,var.get(x))


