#class in python

class  Complex():
     def __init__(self):
           print("hello")
c=Complex()


class Complex():
    def __init__(self,real,img):
         self.r=real
         self.i=img
c=Complex(3,4)
print(c.i)
print(c.r)


class Apollo():
    destination="moon"
    def __init__(self):
        print("ready to launch")


    def flying(self):
            print("spaceship is flying")

    def getdestination(self):
                print("the destination is"+self.destination)
a=Apollo()
a.flying()
a.getdestination()
b=Apollo()
b.destination="mass"
b.getdestination()