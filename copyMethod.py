List = [1,2,3,4,5,'sandhya']
print("print List: ", List)
print("Print id of List: ", + id(List))  #2468861432840

#these 'List' and 'b' values stored in different places

b=List.copy()
print("copy List values into b: ",b)
print("Print id of b: ",id(b))           #2008017875208


#if i want change the value in 'b',after changing also it stores same place for 'b'

b[4] = 'aruna'
print("After changing the b[4]: ", b)
print("Print id of b: ", id(b))          #2008017875208
