from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from tkinter.colorchooser import askcolor
import os
import datetime

from tkinter.filedialog import askopenfilename, asksaveasfilename

master = Tk()
master.title(" FIRST TEXT EDITOR")
menu = Menu(master)
filemenu = Menu(master)
master.config(menu=menu)
menu.add_cascade(label="File", menu=filemenu)
file_name=None
#file functions
def newfile():
        global filename
        filename="first text editor"
        text.delete(1.0,END)

filemenu.add_command(label="Newfile", underline=1, command=newfile, accelerator="Ctrl+N")


def openfile(event=NONE):
    input_file_name=tkinter.filedialog.askopenfilename(defaultextension=".txt")
    if input_file_name:
     global file_name
     file_name=input_file_name
    text.delete(1.0,END)
    with open(file_name) as _file:
        text.insert(1.0, _file.read())
def write_to_file(filename):
    try:
        content = text.get(1.0,'end')
        with open(filename,'w') as the_file:
            the_file.write(content)
    except IOError:
        pass
filemenu.add_command(label="openfile", underline=1, command=openfile, accelerator="Ctrl+O")

def Save_as(event=NONE):
    input_file_name=tkinter.filedialog.asksaveasfilename(defaultextension=".txt")
    global file_name
    if input_file_name:
        filename=input_file_name
        write_to_file(filename)
        master.title("text editor")
        return"break"
def save(event=NONE):
    if not file_name:
        Save_as()
    else:
        write_to_file(file_name)
    return"break"

filemenu.add_command(label="save", underline=1, command=save, accelerator="Ctrl+S")
filemenu.add_command(label="save as", underline=1, command=Save_as, accelerator="Ctrl+S")

def exit():
    master.destroy()
filemenu.add_command(label="Exit", command=exit)
editmenu = Menu(master)
menu.add_cascade(label="Edit", menu=editmenu)

#end

#edit functions
def copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())


editmenu.add_command(label='Copy', accelerator='Ctrl+C', compound='left',  underline=0, command=copy)

def cut():
    text.event_generate("<<cut>>")

editmenu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', underline=0, command=cut)



def paste():
    try:
        teext = text.selection_get(selection='CLIPBOARD')
        text.insert(INSERT, teext)
    except:
        tkinter.messagebox.showerror("Error")

editmenu.add_command(label='paste', accelerator='Ctrl+V', compound='left',  underline=0, command=paste)


def undo():
    text.edit_undo()


editmenu.add_command(label='undo', accelerator='Ctrl+Z', compound='left',  underline=0, command=undo)


def redo():
    text.edit_redo()


editmenu.add_command(label='redo', accelerator='Ctrl+Y', compound='left',  underline=0, command=redo)
editmenu.add_separator()


def delete():
    text.delete(0.0,END)

editmenu.add_command(label='delete', accelerator='Ctrl+del', compound='left', underline=0, command=delete)





#insert
insertmenu = Menu(master)
menu.add_cascade(label="Insert", menu=insertmenu)


def date():
    data = datetime.date.today()
    text.insert(INSERT, data)


insertmenu.add_command(label="Date", command=date)

def time():
    ti=time.gmtime()
    text.clipboard_append(time.asctime(ti))
    insertmenu.add_command(label='Time',command=time)


def line():
    lin = "_" * 60
    text.insert(INSERT, lin)


insertmenu.add_command(label="Line", command=line)



#format
formatmenu = Menu(menu)
menu.add_cascade(label="Format", menu=formatmenu)


def font():
    (triple, color) = askcolor()
    if color:
        text.config(foreground=color)


formatmenu.add_cascade(label="Color...", command=font)
formatmenu.add_separator()


def normal():
    text.config(font=("Arial", 10))


formatmenu.add_radiobutton(label='Normal', command=normal)


def bold():
    text.config(font=("Arial", 10, "bold"))


formatmenu.add_radiobutton(label='bold', command=bold)


def underline():
    text.config(font=("Arial", 10, "underline"))


formatmenu.add_radiobutton(label='underline', command=underline)


def italic():
    text.config(font=("Arial", 10, "italic"))


formatmenu.add_radiobutton(label='italic', command=italic)
#personalize

personalize = Menu(master)

menu.add_cascade(label="Personalize", menu=personalize)


def background():
    (triple, color) = askcolor()
    if color:
        text.config(background=color)


personalize.add_command(label="background color", command=background)
text = Text(master, height=30, width=60, font=("Arial", 10))
scroll = Scrollbar(master, command=text.yview)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)


#start of help Menu
helpmenu = Menu(menu)
menu.add_cascade(label='view', menu=helpmenu)
helpmenu.add_command(label='About', underline=0, command='About')
helpmenu.add_command(label='Help', underline=0, command='Help')
# end of About Menu

master.config(menu=menu)

text.pack()
master.resizable(0, 0)
master.mainloop()