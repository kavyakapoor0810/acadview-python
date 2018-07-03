#create command
import sqlite3
conn = sqlite3.connect('test.db')
print("opened database successsfully")
#insert
# conn.execute(''' CREATE TABLE COMPANY1
             #(ID INT PRIMARY KEY  NOT NULL,
            # NAME    TEXT     NOT NULL,
            # AGE     INT       NOT NULL,
             #ADDRESS CHAR(50),
            # SALARY  REAL)''')
print("table created successfully")
#conn.close()

import sqlite3
#conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
            # values(1,  'paul',32 ,'califonia' , 20000.00)")
#conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
             #values(2 , 'Allen',25 ,'Texas' , 15000.00)")
#conn.commit()
#print("Records created successfully")
#conn.close()
#select
import sqlite3
cursor = conn.execute("SELECT  ID,NAME,AGE,SALARY from company1")
for row in cursor:
    print("ID = ",row[0])
    print("NAME = ",row[1])
    print("AGE = ",row[2])
    print("SALARY =",row[3], "\n")
print("operation done successfully")

#update
import sqlite3
conn.execute("UPDATE COMPANY1 set SALARY =25000.00 where ID = 1")
conn.commit()
print("Total number of rows updated :" , conn.total_changes)
cursor = conn.execute("SELECT  ID,NAME,AGE,SALARY from company1")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("SALARY =", row[3], "\n")
print("operation done successfully")


import sqlite3
conn.execute("UPDATE COMPANY1 set SALARY =25000.00 where ID = 1")
conn.commit()
print("Total number of rows updated :" , conn.total_changes)
cursor = conn.execute("SELECT  ID,NAME,AGE,SALARY from company1")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("SALARY =", row[3], "\n")
print("operation done successfully")


import sqlite3
conn.execute("DELETE COMPANY1 set SALARY =25000.00 where ID = 1")
conn.commit()
print("Total number of rows updated :" , conn.total_changes)
cursor = conn.execute("SELECT  ID,NAME,AGE,SALARY from company")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("SALARY =", row[3], "\n")
print("operation done successfully")
conn.close()







