def cityName():
    city='lincoln'
    print("outer func: " ,  city)
    
    def anotherCity():
       city ='omaha'
       print("inner function: ",city)
    anotherCity()

city='jefferson'  #global variable    
print("outside of both functions: ", city)       
cityName()

print("what is the city: ",city)
    
