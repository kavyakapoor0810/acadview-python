
#question1

print("we represent time in a way that's easy for understand  ,python stores it in tuples, these python tuples are made of nine  numbers"
"index  (0) field (years) value (1995)"   
"index  (1) field (month) value (1 to12)"
" index  (2) field (day) value (1 to31)"
"index   (3)  field (hour) value(0 to 23)"
 "index  (4)   field (minutes) value (0 to59)"
"index   (5)   field (seconds) value(0 to61)"
 "index  (6)  field (day of week) value (0to6)"
 "index  (7)  field  (day of year) value (1 to 366)"
"indeex  (8) field (DST) value (-1,0,1) ")

#question2
import datetime,time
print(time.asctime(time.localtime()))

#question3
import datetime
from datetime import date
d=date.today()
print(d.month)

#question4
import datetime
d=datetime.date.today()
print(d.day)

#question5

import datetime
d=datetime.date.today()
d.strftime("%d%m%y")
print(d.day)

#question6

import datetime,time
print(time.asctime(time.localtime()))

#question7

import math
a=int(input("enter the number"))
print(math.factorial(a))

#question8

import math
a=int(input("number:"))
b=int(input("number:"))
print(math.gcd(a,b))

#question9

import os
print(os.getcwd())
print(os.environ)

