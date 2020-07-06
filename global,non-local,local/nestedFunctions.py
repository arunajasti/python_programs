def outer():
    city='lincoln'
    print('outer func : ' ,city)#1

    def inner():
        global city
        city='jefferson'
        print ("after calling inner(): ", city)#4
    print("before calling inner():" ,city)#2
    print("calling inner()") #3        
    inner()#5
    print(city)#it print after inner() print   
outer()
print("what is the city: ",city)#6 prints inner city name

print()
#2

def outer():
    city='lincoln'
    print('outer func : ' ,city)#1

    def inner():
        global city
        city='jefferson'
        #print ("after calling inner(): ", city)#4
    print("before calling inner():" ,city)#2
    print("calling inner()") #3
    inner()
    print ("after calling inner(): ", city)#4
      
outer()
print("what is the city: ",city)#5 prints inner city name'''
