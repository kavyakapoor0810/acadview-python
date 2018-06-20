
#question1
radius=float(input("enter radius"))
def  area(rad):
    area=3.14*rad*rad
    return area
ar=area(radius)
print(ar)


#question2
n=6
def perfect(n):
 sum = 0
 for i in range (1,n):
    if(n%i ==0):
        sum=sum+i
 if(sum==n):
     return True
 else:
        return False
print(perfect(n))
for i in range(1,1001):
    if(perfect(i)==True):
        print(i)

#question3
def  mul_table(n, i=1):
    print(n*i)
    if  i  !=10:
        mul_table(n,i+1)
mul_table(12)

#question4

def power(a,b):
    if b==1:
        return a
    else:
        return a* power(a,b-1)
a=int(input("enter a:"))
b=int(input("enter b:"))
print("result:",power(a,b))


#question5
DIC = {"factorial up to 10 =":[]
       }

def factorial():
    f=1
    for i in range(1,11):
        f = f *i
        DIC["factorial up to 10 ="].append(f)
    print("factorial up to 10 =" ,f)
factorial()
print(DIC)


