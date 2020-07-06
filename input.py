first_name = input("Enter the Firstname")#input is string
last_name = input("Enter the Lastname")
fullname = first_name + last_name
print("UserName: " + fullname)

first_num = int(input("Enter the FirstNum"))#converting input into int to add the numbers
second_num = int(input("Enter the SecondNum"))
result = first_num + second_num
print(result)


#eval
x=eval(input("Enter the age: "))
if x>=18:
    print("He/She eligible for voting")
else:
    print("not eligible for voting")
print(type(x))
print(x)
