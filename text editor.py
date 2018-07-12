from tkinter import *
from tkinter.filedialog import *
import tkinter
root = Tk()
#filename = None
#text = StringVar()



def newfile():
    global filename
    filename="untitled"
    text.delete(1.0,END)



def saveFile():
    global filename
    t=text.get(1.0,END)
    f=open(filename,'w')
    f.write(t)
    f.close()

def saveAs():
    f=asksaveasfile(mode='w',defaultextension='.txt')
    t=text.get(0.0,END)
    try:
       f.write(t.rstrip())
    except:
        showerror(title="Oops!",message="Unable to save file...")

def openfile():
    f=askopenfile(mode='r')
    t=f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)

#root = Tk()
root.title("My text Editor")
root.minsize(width=400,height=400)
root.maxsize(width=400,height=400)

#text = Text(root,width=400,height=400)
#text.pack()

text = Text(root)
text.pack()

menubar=Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="save",command=saveFile)
filemenu.add_command(label="saveAs",command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="quit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)
root.mainloop()













