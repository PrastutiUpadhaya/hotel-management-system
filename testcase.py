import sqlite3
from sqlite3 import Error
from tkinter import *
import tkinter.messagebox

#banker()
def sql_connection():
    try:
        con = sqlite3.connect('database.db')
        return con
    except Error:
        print(Error)

def create_db(con):
    cursorObj=con.cursor()
    """" 
    cursorObj.execute("create table if not exists branches (BID varchar(5) PRIMARY KEY, branch_name varchar(20), location varchar(10))")
    cursorObj.execute("insert into branches values('B1', 'Voyage Modern', 'New Delhi')")
    cursorObj.execute("insert into branches values('B2', 'Voyage Sea', 'Mumbai')")
    cursorObj.execute("insert into branches values('B3', 'Voyage Maples', 'Chennai')")
    cursorObj.execute("insert into branches values('B4', 'Voyage Luxury', 'Kolkata')")
    cursorObj.execute( "select * from branches")
    print(cursorObj.fetchall())

    cursorObj.execute("create table if not exists rooms (Room_No varchar(5), BID varchar(5), No_Of_Beds integer, Price integer, Status varchar(2), View varchar(3), primary key (Room_no, BID))")
    cursorObj.execute("insert into rooms values ('R1', 'B1', 1, 3000, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R2', 'B1', 2, 5000, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R3', 'B1', 3, 7000, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R4', 'B1', 1, 3500, 'A', 'Yes')")
    cursorObj.execute("insert into rooms values ('R5', 'B1', 2, 6000, 'A', 'Yes')")
    cursorObj.execute("insert into rooms values ('R6', 'B1', 3, 8000, 'A', 'Yes')")

    cursorObj.execute("insert into rooms values ('R1', 'B2', 1, 2500, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R2', 'B2', 2, 3000, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R3', 'B2', 3, 6500, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R4', 'B2', 1, 3000, 'A', 'Yes')")
    cursorObj.execute("insert into rooms values ('R5', 'B2', 2, 4000, 'A', 'Yes')")
    cursorObj.execute("insert into rooms values ('R6', 'B2', 3, 7700, 'A', 'Yes')")

    cursorObj.execute("insert into rooms values ('R1', 'B3', 1, 2000, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R2', 'B3', 2, 3500, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R3', 'B3', 3, 4000, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R4', 'B3', 1, 2500, 'A', 'Yes')")
    cursorObj.execute("insert into rooms values ('R5', 'B3', 2, 4000, 'A', 'Yes')")
    cursorObj.execute("insert into rooms values ('R6', 'B3', 3, 5500, 'A', 'Yes')")

    cursorObj.execute("insert into rooms values ('R1', 'B4', 1, 2000, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R2', 'B4', 2, 3000, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R3', 'B4', 3, 4000, 'A', 'No')")
    cursorObj.execute("insert into rooms values ('R4', 'B4', 1, 2500, 'A', 'Yes')")
    cursorObj.execute("insert into rooms values ('R5', 'B4', 2, 3600, 'A', 'Yes')")
    cursorObj.execute("insert into rooms values ('R6', 'B4', 3, 4500, 'A', 'Yes')")

    con.commit()

    cursorObj.execute( "select * from rooms")
    print(cursorObj.fetchall())

    cursorObj.execute("create table  reservations (Room_No varchar(5), BID varchar(5), check_in_date date, check_out_date date)")
    cursorObj.execute("insert into reservations values ('R1', 'B4','2000-10-11','2000-10-13')")
    cursorObj.execute("insert into reservations values ('R1', 'B4','2000-10-09','2000-10-10')")
    cursorObj.execute("insert into reservations values ('R1', 'B4','2000-10-01','2000-10-05')")
    
    cursorObj.execute("select room_no ,bid, sum(not(check_out_date<'2000-10-23' or check_in_date>'2000-10-25'))=0 from reservations  group by room_no, bid")
    rows=cursorObj.fetchall()
    print(len(rows))
    print(rows)
    for row in rows:
        if row[0]=='R1' and row[1]=='B4' and row[2]==0 :
            print(row[0])

    print(cursorObj.fetchall())
   
    cursorObj.execute("create table  customers ( cust_id integer PRIMARY KEY , fname varchar(100) , lname varchar(100), email varchar(100) , country varchar(100), phoneno integer)")  

    cursorObj.execute("insert into customers values (1, 'khushi','gupta','khushi123@gmail.com' , 'india',9818303920 )")
    cursorObj.execute("drop table reservations ")
    cursorObj.execute("create table  reservations (cust_id  integer , Room_No varchar(5), BID varchar(5), check_in_date date, check_out_date date)")
    cursorObj.execute("insert into reservations values ( 1, 'R1', 'B4','2000-10-11','2000-10-13')")
    cursorObj.execute("insert into reservations values ( 1 ,'R1', 'B4','2000-10-09','2000-10-10')")
    cursorObj.execute("insert into reservations values ( 1, 'R1', 'B4','2000-10-01','2000-10-05')")
"""
    cursorObj.execute("select * from reservations")
    print(cursorObj.fetchall())


    con.commit()
    con.close()
con = sql_connection()

create_db(con)
