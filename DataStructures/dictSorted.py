dict1 = {'b':2,'a':3,'d':1,'c':4}
print(sorted(dict1.items())) #sorted  the order by keys
print(sorted(dict1.keys()))  #retrieve only keys in sorted order
print(sorted(dict1.values())) #retrieve only values in sorted order
print(sorted(dict1.items(),key = lambda x:(x[1],x[0])))#it sorted the order by values
#o/p
[('a', 3), ('b', 2), ('c', 4), ('d', 1)]
['a', 'b', 'c', 'd']
[1, 2, 3, 4]
[('d', 1), ('b', 2), ('a', 3), ('c', 4)]


#print(dict1.sort()) there is sort() in dict
