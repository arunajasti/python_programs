def addNumbersInList(numbers):
     total = 0
     for x in numbers:
     	total=total+x
     return total
    
print(addNumbersInList([10,20,30]))

print("count odd numbers in list")

def countodd(numbers):
    oddcount=0
    for x in numbers:
        if x%2!=0:
            oddcount+=1
    return oddcount
print(countodd([1,4,3,9]))


print("removefirstandlastnumbers")

def removeFirstAndLast(numbers):
     alist = []
     for x in numbers:
         alist.append(x)
     print( alist)
   
     #new=alist.copy()
     alist.pop(0)
     print(alist)
     alist.pop()
     print(alist)

removeFirstAndLast([2,3,4,5])

print("another way")
def removeFirstAndLast1(numbers):
     if len(numbers) == 0:
          return
     else:
          del numbers[0]

     if len(numbers) <= 0:
          return numbers

     else:
          del numbers[len(numbers)-1]
          return numbers
print(removeFirstAndLast1([10,20,30,40]))
            
