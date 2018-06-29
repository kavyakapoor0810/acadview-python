
#f=open("test.txt","r")
#print(f.read())

#print(f.readline())
#print(f.readlines())


f=open("test.txt","a")
#f.write("hello")
l=["a","b","c"]
f.writelines(l)
l=["a\n","b\n","c\n"]
f.writelines(l)

with open("test.txt","r")as f:
 print(f.readline())
 print(f.read(6))
 print(f .tell())
 f.seek(0,0)
 print(f.tell())

