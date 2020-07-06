f = open('file.txt','r')
for x in (f.readlines()):
    print(x)
f.close()
