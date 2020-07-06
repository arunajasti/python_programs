n=int(input("Enter the Number: "))
def fact(n):
    if(n==1):
        return n
    else:
        return n*fact(n-1)
print("Factorial of : ",fact(n))
