#question1

import tkinter as tk
from tkinter import *
m = tk.Tk()
m.title("info")
dict={'name':'megha','mobile_number':217895}
scrollbar=Scrollbar(m)
scrollbar.pack(side=LEFT,fill=Y)
mylist=Listbox(m,yscrollcommand = scrollbar.set)
for key in dict. __iter__():
         mylist.insert(END,key)
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
def m():
    m.quit()
b=Button(m,text="enter",command=m)
b.pack()
m.mainloop()


#question2
def megha():
    dict.update({"age":25})
    print(dict)
buton1 =Button(m,text='good',command=megha())
buton1.pack()
m.mainloop()



