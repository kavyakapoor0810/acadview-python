#question1

year=int(input("enter year"))
if(year%4==0):
   print("leap year")
else:
   print("not leap year")

#question2
l=int(input("enter length"))
b=int(input("enter breadth"))
if(l==b):
    print("dimensions are of square")
else:
    print("dimensions are of rectangle")

#question3
a=int(input("enter age"))
b=int(input("enter age"))
c=int(input("enter age"))
if(a>b):
    if(a>c):
        print("a is oldest")
elif(b>a and b<c):
    print("a is youngest")
else:
    print("b is oldest")
#question4
points=int(input("number scored"))
if(a<=50):
    print (" sorry! no prize")
    if(a>50 and a<=150):
     print("congratulations you won a wooden dog")
elif(a>151 and a<=180):
    print("book")
if(a>181 and a<=200):
    print("choclates")

#question5
a=int(input("enter the quantity of item"))
c=a*100
if(c>1000):
    c= c*100-c/10
    print("discount given is")
    print(c)
    print("coast after discount is")
    print(c)
else:
    print("sorry no discount given")

