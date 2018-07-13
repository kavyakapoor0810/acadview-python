from datetime import date
import time

def date_():
    data = date.today()
    print(data)
    #text.insert(INSERT, data)


#insertmenu.add_command(label="Date", command=date)

def time_():
    ti=time.asctime(time.gmtime())
    print (ti)
    #text.clipboard_append(time.asctime(ti))
    #insertmenu.add_command(label='Time',command=time)

date_()
time_()