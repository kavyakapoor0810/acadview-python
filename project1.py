from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import simpledialog
import time


#functions
def newfile():
    global filename
    filename="Untitled"
    text.delete(0.0,END)


def savefile():
        global filename
        t = text.get(0.0, END)
        f = open(filename, mode='w')
        f.write(t.strip())
        f.close()

def saveAs():
        f = asksaveasfile(mode='w', defaultextension='.txt')
        t = text.get(0.0, END)
        try:
            f.write(t.strip())
        except:
            showerror(title='oops', message='unable to save file')

def openfile():
        f = askopenfile(mode='r')
        t = f.read()
        text.delete(0.0, END)
        text.insert(0.0, t)

def exit():
        if messagebox.askyesno("quit", "are you want to quit"):
            masster.destroy()

def About():
        label = messagebox.showinfo("about", " A text editor is just like a notepad")

def findin():
        findString = simpledialog.askstring('Find', 'enter a text')
        t = text.get(0.0, END)

        # count=0
        occurences = t.upper().count(findString.upper())
        if t.upper().count(findString.upper()) > 0:
            label = messagebox.showinfo("RESULTS", findString + 'has multiple occurences' + "" + str(occurences))

        else:
            label = messagebox.showinfo('has nooccurences')
            print(t.upper().count(findString.upper()))

#
def cut():

     text.event_generate("<<cut>>")

def copy():
    text.event_generate("<<copy>>")

def paste():
    text.event_generate("<<paste")

def delete():
    text.delete(0.0,END)

def undo():
    text.edit_undo()


def redo():
    text.edit_redo()

def tim():
    ti=time.gmtime()
    text.clipboard_append(time.asctime(ti))
    text.event_generate("<<paste>>")

####
master=Tk()
master.title("TEXT EDITOR")
text=Text(master,width=80,height=80)
text.pack()
menu=Menu(master)
master.config(menu=menu)
filemenu=Menu(menu)
filemenu=Menu(menu)
menu.add_cascade(label='file',menu=filemenu)
menu.add_cascade(label= 'new',command=newfile)
menu.add_cascade(label='save',command=savefile)
menu.add_cascade(label='SaveAs',command=SaveAs)
menu.add_cascade(label='Find',command=findin)
filemenu.add_separator()
filemenu.add_cascade(label="Quit",command=exit)
editmenu=Menu(master)

menu.add_cascade(label='Edit',menu=editmenu)
menu.add_cascade(label='Undo',command=undo)
menu.add_cascade(label='Redo',command=redo)
menu.add_cascade(label='Cut',command=cut)
menu.add_cascade(label='Copy',command=copy)
menu.add_cascade(label='Paste',command=paste)
menu.add_cascade(label='Delete',command=delete)
editmenu.add_separator()
editmenu.add_command(label='Replace')
editmenu.add_separator()
editmenu.add_command(label='Select all')
editmenu.add_command(label='Time and Date',command=time)



helpmenu=Menu(master)
menu.add_cascade(label='help',menu=helpmenu)
helpmenu.add_cascade(label='help')
helpmenu.add_command(label='About',command=About)

master.mainloop()








