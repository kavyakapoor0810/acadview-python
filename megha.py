from tkinter import *
import os
import tkinter.filedialog
import tkinter.messagebox
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename
import datetime
from datetime import date
import time



master = Tk()
master.iconbitmap('icons/favicon.ico')

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
filemenu.add_command(label="openfile", underline=1, command=openfile, accelerator="Ctr+0")

def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),("HTML", "*.html"),("CSS", "*.css"),("JavaScript", "*.js")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        master.title('{} - {}'.format(os.path.basename(file_name),"First text editor"))
    return "break"

def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"

filemenu.add_command(label="save", underline=1, command=save, accelerator="Ctrl+S")
filemenu.add_command(label="save as", underline=1, command=save_as, accelerator="Ctrl+S")

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
    text.event_generate("<<Cut>>")

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


def date_():
    data = date.today()
    #print(data)
    text.insert(INSERT, data)


insertmenu.add_command(label="Date", command=date_)

def time_():
    ti=time.asctime(time.gmtime())
    text.insert(INSERT,ti)
insertmenu.add_command(label='Time',command=time_)

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
# end of help Menu



# ICONS
new_file_icon = PhotoImage(file='icons/newfile.gif')
#openfile_icon = PhotoImage(file='icons/open_file.gif')
savefile_icon = PhotoImage(file='icons/save.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')

icon_frame=Frame(master,height=20)
icon_frame.pack(expand='no',fill='x')
#D:\assignment\icons\cut.gif
#adding shortcut icons
icons=( 'newfile','save', 'cut', 'copy', 'paste','undo', 'redo')
for i, icon in enumerate(icons):
    tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon)).zoom(2,2)
    cmd = eval(icon)
    tool_bar = Button(icon_frame, image=tool_bar_icon, height=35,width=35, command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side='left')


line_number_bar = Text(master, width=4, padx=3, takefocus=0, fg='white', border=0, background='#282828', state='disabled',wrap='none')
line_number_bar.pack(side='left', fill='y')


master.config(menu=menu)

text.pack()
master.resizable(0, 0)
master.mainloop()