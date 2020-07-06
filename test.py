z,x,y = 2,1,0
x,z   = z,y    #2,0 -->x,z
y     = y-z    #0-0
print(x,y,z)
#o/p 2 0 0

print()

val = 1
val2 = 0

val = val ^ val2
print(val)
val2 = val ^ val2
print(val2)
val = val ^ val2
print(val)

#o/p 0
