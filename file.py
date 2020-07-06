
#f=open('aruna.txt','r')

#it gives error because aruna.txt is not exist on desktop/somewhere in sys
# so i want run the program with out abruptly so i used try,except

try:
    f = open('aruna.txt','r')
    print("try")#it won't print because previous stmt raised the exception so it goes except block and the interpretor wont come back again
except FileNotFoundError as msg:
    print(msg)

finally:
    print("finally block executed")





