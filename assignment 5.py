

#question1
for  i  in  range(1,10):
    print(input("enter the values"))
    print(i)

#question2
x="true"
while(x== "rue"):
    print("loop is infinite")

#question3
l=[]
a=int(input("enter the input"))
b=int(input("enter the input"))
l.append(a)
l.append(b)
for i in l:
    print(i**2)


#question4
list = ["apple" ,1 ,"name" ,"hello" ,2.2 ,4 ,"qwerty"]
Int =[]
String =[]
Float =[]
for i in list:
    if isinstance(i,int):
        Int.append(i)

    elif  isinstance(i,str):
        String.append(i)

    else:
        Float.append(i)

print(Float)
print(Int)
print(String)
print("Float list =" +str(Float))
print("Int list = " +str(Int))
print("String list = " + str(String))

#question5
even=[]
odd=[]
for i in range(0,101):
    if i %2==0:
        even.append(i)
    else:
        odd.append(i)
print("number is even",even)
print("number is odd",odd)

#question6
for i in  range(0,4):
    for i in range(0,i+1):
        print("*",end=" ")
    print()

#question7
dictionary={"name":"megha","age":"21"}
for i in dictionary:
    dictionary.get(i)
    print(i)

#question8
l=[]
for i in range(0,5):
    num=int(input("enter the number:"))
    l.append(num)
print(l)
l2=[]
a=int(input("enter the value:"))
x=l.index(2)
x =l.remove(2)
print(l)





