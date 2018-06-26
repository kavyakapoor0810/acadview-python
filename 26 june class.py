#threads in python

import threading
import time
'''class mythread(threading.Thread):
    def __init__(self ,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        print("value send ", self.h)
#time.sleep(5)
thread1 = mythread(1)
thread1.start()
time.sleep(5)
thread2 = mythread(2)
thread2.start()
'''
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        time.sleep(1)
        print("No is ",self.h)
for i in range(10):
    thread1=mythread(i)
    thread1.start()
    thread1.join()

print("active threads are ",threading.active_count())


