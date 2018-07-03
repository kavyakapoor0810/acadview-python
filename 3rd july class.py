
import tkinter
m = tkinter.Tk()
m.mainloop()

import tkinter as tK
r = tK.Tk()
r.title('Counting Seconds')
button = tK.button(r ,text='Stop',width=25,command=r.destroy)
button.pack()
r.mainloop()