a=[1,1]
b=[2,2]
c=a+b*3
print(c)

print("cumulative sum")
def calCumulativeSum(numbers): 
	sum=[]
	total =0
	for x in numbers:
		total+=x
		sum.append(total)
print(sum)

calCumulativeSum([1,2,3])
