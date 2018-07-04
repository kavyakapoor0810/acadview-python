#question1

import tkinter as tk
from tkinter import *
kav = tk.Tk()
kav.title("info")
dict={'name':'megha','mobile_number':217895}
scrollbar=Scrollbar(kav)
scrollbar.pack(side=LEFT,fill=Y)
mylist=Listbox(kav,yscrollcommand = scrollbar.set)
for key in dict. __iter__():
         mylist.insert(END,key)
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
def kavy():
    kav.quit()
b=Button(kav,text="enter",command=kavy)
b.pack()
kav.mainloop()


#question2
def megha():
    dict.update({"age":25})
    print(dict)
buton1 =Button(kav,text='good',command=megha())
buton1.pack()
kav.mainloop()



