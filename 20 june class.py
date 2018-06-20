#functions
def fn():
    print("hello")
fn()

def fn(a):
    print(a)#call by reference
fn("hello world")



# three types of parameters (required ,keyword,default)

def add(a,b):
      c=a+b
      print(c)
a=2
b=3
add(a=2,b=3)

def  add(a,b=2):
    d=a*a
    c=b*b*b
    print(d,c)
#add(2)

      return d,c
 a,b=add(2,3)
 print(a+" "+b)
 print(str(a)+" "+str(b))








