f = open('file.txt','r')
print(f.mode)       # r
print(f.name)       # file.txt
print(f.readable()) # true becoz readmode
print(f.writable()) # false becoz iy is readmode file
f.close()
print(f.closed)     # true

print()

#if you execute this program the file.txt will be empty why f.write() i not using in this  so it overwrite
#so execute 'write' file again so it appears text in file.txt
#whenever you execute 'w' mode file it overwrite
f = open('file.txt','w') 
print(f.mode)        # w
print(f.name)        # file.txt
print(f.readable())  # false
print(f.writable())  # true
#f.close()
print(f.closed)      #its false because f.close() is written after this stmt
f.close()            # false
