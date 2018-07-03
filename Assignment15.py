#question1

import sqlite3
conn=sqlite3.connect("test.db")
print("opened database successfully")
#conn.execute('''CREATE TABLE BOOK3
            #(BOOKID INT PRIMARY KEY NOT NULL,
            #TITLEID INT             NOT NULL,
            #LOCATION VARCHAR        NOT NULL,
            #GENRE     TEXT          )''')
print("table1 created successfully")

#conn.execute('''CREATE TABLE TITLES
            #(TITLEID INT PRIMARY KEY NOT NULL,
           # TITLE    TEXT            NOT NULL,
            #ISBN     VARCHAR         NOT NULL,
            #PUBLISHERID INT          NOT NULL,
            #PUBLICATIONYEAR INT      NOT NULL)''')
print("table 2 created successfully")

#conn.execute('''CREATE TABLE PUBLISHERS
            #(PUBLISHERID INT PRIMARY KEY  NOT NULL,
            #NAME         TEXT             NOT NULL,
            #STREETADDRESSS  VARCHAR       NOT NULL,
           # ZIPCODEID       INT           NOT NULL)''')
print("table3 created successfully")

#conn.execute(''' CREATE TABLE ZIPCODES
             #(ZIPCODEID  INT PRIMARY KEY     NOT NULL,
             #CITY         VARCHAR            NOT NULL,
           # STATE         VARCHAR           NOT NULL,
             #ZIPCODE       VARCHAR           NOT NULL)''')
print("table4 created successfully")

#conn.execute(''' CREATE TABLE AUTHORTITLE
             #(AUTHORTITLEID    INT PRIMARY KEY NOT NULL,
            # AUTHORID           INT           NOT NULL,
            # TITLEID            INT          NOT NULL)''')
print("table5 created successfully")

#conn.execute(''' CREATE TABLE AUTHORS
            #(AUTHORID    INT      NOT NULL,
           # FIRST NAME  VARCHAR   NOT NULL,
           # MIDDLE NAME  VARCHAR  NOT NULL,
           # LAST  NAME   VARCHAR  NOT NULL)''')
print("table 6 created successfully")



#conn.execute("INSERT INTO BOOK3(BOOKID,TITLEID,LOCATION,GENRE)\
             #values(67, 5, 'KARNAL','economics')")
#conn.execute("INSERT INTO BOOK3(BOOKID,TITLEID,LOCATION,GENRE)\
            # values(55, 8, 'YNR','history')")
#conn.commit()
print("Records created successfully")



#conn.execute("INSERT INTO AUTHORS(AUTHORID,FIRST NAME,MIDDLE LAST NAME)\
             #values(50, MEGHA, 'KOMA;','AHUJA')")
#conn.execute("INSERT INTO AUTHORS(AUTHORID,FIRST NAME,MIDDLE NAME,LAST NAME)\
            # values(45, RAMAN, 'DEEP','SINGH')")
#conn.commit()
#print("Records created successfully")


conn.execute("UPDATE BOOK3 set TITLEID=8 where BOOKID=55")
conn.commit()
print("total number of rows updated",conn.total_changes)

cursor=conn.execute("SELECT BOOKID,TITLEID,LOCATION,GENRE FROM BOOK3")
for row in cursor:
    print("BOOKID=",row[0])
    print("TITLEID=",row[1])
    print("LOCATION=",row[2])
    print("GENRE=",row[3], "\n")
print("operation done successfully")
conn.close()