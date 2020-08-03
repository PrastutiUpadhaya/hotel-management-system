from tkinter import *
import tkinter.messagebox
from PIL import ImageTk
#from  data import *
import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
        con = sqlite3.connect('database.db')
        return con
    except Error:
        print(Error)


def reserve():
    def customerlogin():
        con = sql_connection()
        c = con.cursor()
        c.execute("SELECT count(*) FROM CUSTOMERS")
        row = c.fetchall()  # return all the records as tuple therefore it is a tuple which is a collection of tuples
        id = 1 + row[0][0]
        """  f = efn.get()
        l = eln.get()
        e = eei.get()
        c = ecn.get()
        p = epn.get()
        r = roomno.get()
        b = brname.get()
        ci=cid.get()
        co=cod.get()
        """
        f = efn.get()
        l = eln.get()
        e = eei.get()
        cn = ecn.get()
        p = epn.get()
        r = roomno.get()
        b = brname.get()
        ci = cid.get()
        co = cod.get()

        c.execute("INSERT INTO CUSTOMERS VALUES(" + str(id) + ",'" +str( f) + "','" + str(l) + "','" + str(e) + "','" + str(cn) + "'," + str(p) + ")")
        # get the branch id from the branch name
        c.execute("select bid from  branches  where location = '"+ str(b) +"'")
        r1 = c.fetchall()
        c.execute("INSERT INTO reservations  VALUES(" + str(id) + ",'" + str(r) + "','" + str(r[0]) + "','" + str(ci) + "','" + str(co) + "')")
        con.commit()

        # connection.commit()
        # This method commits the current transaction. If you don't call this method, anything you did since the last call to commit() is not visible from other database connections.
        tkinter.messagebox.showinfo("DONE", "CUSTOMER ID is : " + str(id))
        con.close()

    window=Toplevel()
    window.geometry("1700x1500")
    window.title("Profile")

    canvas=Canvas(window,width=300,height=300)
    canvas.pack(fill=BOTH, expand=TRUE)
    img = ImageTk.PhotoImage(file="background1.png")
    canvas.create_image(0,0,image=img, anchor=NW)

    efn = StringVar()
    eln = StringVar()
    ecn = StringVar()
    eei = StringVar()
    epn = IntVar()
    roomno = StringVar()
    brname = StringVar()
    cid = StringVar()
    cod = StringVar()

    label1=Label(window,text="First Name : ",bg="#f5c2a9",width=20,font=("comic sans",10,"bold" ),relief="groove")
    label1.place(x=400,y=200)
    ent1=Entry(window,textvar=efn).place(x=600,y=200)
    label2=Label(window,text="Last Name : ",bg="#f5c2a9",width=20,font=("comic sans",10,"bold" ),relief="groove")
    label2.place(x=400,y=250)
    ent2=Entry(window,textvar=eln).place(x=600,y=250)
    label3=Label(window,text="Email : ",bg="#f5c2a9",width=20,font=("comic sans",10,"bold" ),relief="groove")
    label3.place(x=400,y=300)
    ent3=Entry(window,textvar=eei).place(x=600,y=300)

    label4=Label(window,text="Country : ",bg="#f5c2a9",fg="black",width='20',font=("comic sans",10,"bold" ),relief="groove")
    label4.place(x=400,y=350)
    ent4=Entry(window,textvar=ecn).place(x=600,y=350)
    label5=Label(window,text="Phone Number",bg="#f5c2a9",fg="black",width='20',font=("comic sans",10,"bold" ),relief="groove")
    label5.place(x=400,y=400)
    ent5=Entry(window,textvar=epn).place(x=600,y=400)
    label6 = Label(window, text="Room number", bg="#f5c2a9", width=20, font=("comic sans", 10, "bold"), relief="groove")
    label6.place(x=400, y=450)
    ent6 = Entry(window, textvar=roomno).place(x=600, y=450)
    label7 = Label(window, text="Branch ", bg="#f5c2a9", width=20, font=("comic sans", 10, "bold"), relief="groove")
    label7.place(x=400, y=500)
    list = ["Mumbai", "Delhi", "Pune", "Bangalore", "Rajasthan"]
    droplist = OptionMenu(window, brname, *list)
    brname.set("Select the branch")
    droplist.configure(width=20)
    droplist.place(x=600, y=500)
    label8 = Label(window, text="Check In Date : ", bg="#f5c2a9", width=20, font=("comic sans", 10, "bold"), relief="groove")
    label8.place(x=400, y=550)
    ent8 = Entry(window, textvar=cid).place(x=600, y=550)
    label9 = Label(window, text="Check Out Date : ", bg="#f5c2a9", width=20, font=("comic sans", 10, "bold"),relief="groove")
    label9.place(x=400, y=600)
    ent9 = Entry(window, textvar=cod).place(x=600, y=600)
    but1=Button(window,text="BOOK NOW ",width=20,bg="black",fg="white",font=("comic sans",15,"bold" ),command=customerlogin ).place(x=800, y=600) #command=djvhdajsvk
    window.mainloop()
