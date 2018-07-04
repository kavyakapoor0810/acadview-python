'''

#GuI part2
#menu button
from tkinter import *
top = Tk()
mb = Menubutton (top,text = "Menu")
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb['menu'] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton( label ='Contact',variable = cVar)
mb.menu.add_checkbutton( label ='About',variable = aVar)
mb.pack()
top.mainloop()
'''
'''
from  tkinter import  *
root=Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open---')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()
'''
'''
#message
from tkinter import *
main = Tk()
ourMessage = 'This is our Message'
messageVar = Message(main,text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
main.mainloop()
'''
'''
#radio button
import tkinter as tk
root = tk.Tk()
V = tk.IntVar()
tk.Label(root,text=""" Choose a programming language:""").pack()
tk.Radiobutton(root,text="python",variable=V,value=1).pack(anchor=tk.W)
tk.Radiobutton(root,text="perl",variable=V,value=2).pack(anchor=tk.W)
root.mainloop()
'''
'''
#scale
from tkinter import *
master = Tk()
w = Scale(master, from_=0, to=42)
w.pack()
w=Scale(master ,from_=0 ,to=200)
w.pack()
w=Scale(master ,from_=0,to=200,orient=HORIZONTAL)
w.pack()
mainloop()
'''


'''
#scrollbar
from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT,fill= Y)
mylist = Listbox(root,yscrollcommand = scrollbar.set)
for line in range(100):
    mylist.insert(END, 'This is line number'+str(line))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()
'''
'''
from tkinter import *
root=Tk()
root.title('ruby')
top=Toplevel()
top.title('python')
top.mainloop()
'''

'''
from tkinter import *
m1 = PanedWindow()
m1.pack(fill =  BOTH,expand = 1)
left = Entry(m1, bd =5)
m1.add(left)
m2 = PanedWindow(m1 , orient = VERTICAL)
m1.add(m2)
top = Scale(m2,orient = HORIZONTAL)
m2.add(top)
mainloop()
'''

#message box

from tkinter import *
from tkinter import  messagebox
def show():
    messagebox.showerror("title","desc")
root=Tk()
Button(root,command=show())