
#question1
import threading
from  threading import Thread
import time
class Th(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        time.sleep(5)
        print("hello i am running",self.h)
obj1 = Th(1)
obj1.start()
obj2 = Th(2)
obj2.start()

#question2

import threading
from threading import Thread
import time
class Th(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        print("number is = ",self.h)
for i in range(1,11):
    thread = Th(i)
    time.sleep(1)
    thread.start()

#question3
import threading
import time
class Mythread(threading.Thread):
    def __init__(self,value):
        threading.Thread.__init__(self)
        self.v=value
    def run(self):
        a=(2,4,6,8,10)
        for i in range(0,5):
            print(self.v[i])
            time.sleep(a[i])
thread1=Mythread([1,2,3,4,5])
thread1.start()

#question4
import threading
import time
import math
class Mythread(threading.Thread):
    def __init__(self,value):
        threading.Thread.__init__(self)
        self.v=value
    def run(self):
        print(math.factorial(self.v))
thread1=Mythread(7)
thread1.start()
