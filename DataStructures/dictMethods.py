dict1 = {'school':'RVR',1:'Rank','grade':'A',2:'college'}
print("Print keys and values: ", end="")#end these 2 print stmts works in single lin
print(dict1)

#retrieve without using method
print("retrieve the value of school dict1['school']: ",end="")
print(dict1['school'])

#modify without using method

dict1['school']='NRH'
print("modify the value of 'RVR' as 'NRH' dict['school']='NRH': " ,end="")
print(dict1)

#add keys and values without using method there is update() also
dict1['tutor']='math'
print("After adding the tutor key into dict1['tutor']='math': ",dict1)

#keys()
print("Keys only dict1.keys(): ", dict1.keys())
print(type(dict1.keys()))


#values()
print("values only dict1.values(): ", dict1.values())
print(type(dict1.values()))


#items()

print("Keys & values dict1.items(): ", dict1.items())
print(type(dict1.items()))

#get()
print("get the grade value dict1.get('grade'): " ,dict1.get('grade'))
print("get the grade value dict1.get('activities'): " ,dict1.get('activities'))
#there is no activities key in dict1, but it wont give error,it gives None


#popitem()
print("remove last item using popitem(): " ,dict1.popitem())
print(dict1)

#pop(argument) you can remove specific key
print("remove the key '1' pop(1): " ,dict1.pop(1))
print(dict1)
