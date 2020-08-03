from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from sqlite3 import *
import sqlite3
#from data import *
def sql_connect2():
    try:
        con2 = sqlite3.connect('database.db')
        return con2
    except Error:
        print(Error)


def check():
    def check_availabilty():
        con2 = sql_connect2()
        c = con2.cursor()
        # if the room is unoccupied
        b1 = var1.get()
        nob = var2.get()
        v = radio_var.get()
        ind = cid1.get()
        outd = cod1.get()
        # ("SELECT BID FROM BRANCHES WHERE(b1=location)")
        c.execute("SELECT * FROM ROOMS R1 WHERE (R1.No_Of_Beds=" + str(nob) + ") AND (R1.VIEW='" + str(
            v) + "') AND (R1.BID=(SELECT BID FROM BRANCHES WHERE(location = '" + str(b1) + "'))) AND R1.STATUS='A'")
        rows = c.fetchall()
        alpha = rows
        if (len(rows) == 0):
            c.execute(
                "select room_no ,bid, sum(not(check_out_date<'2000-10-23' or check_in_date>'2000-10-25'))=0 from reservations  group by room_no, bid")
            rows = c.fetchall()
            for row in rows:
                if row[0] == 'R1' and row[1] == 'B4' and row[2] == 1:
                    # print(row[0])
                    tkinter.messagebox.showinfo(" AVAILABLE ",
                                                "The room(number=" + row[
                                                    0] + "  )  is available . Remember the room number in case you want to reserve the room .")
            if len(rows) == 0:
                tkinter.messagebox.showinfo("NOT AVAILABLE ", "The room is NOT available during the required period")


        else:
            tkinter.messagebox.showinfo(" AVAILABLE ",
                                        "The room(number=" + alpha[0][
                                            0] + " )  is available.Remember the room number in case you want to reserve the room .")

    root = Toplevel()
    root.geometry("1700x1500")#resize
    root.title("AVAILABILITY STATUS ")
#root.configure(background="#e6edf5")
#img = PhotoImage(file="")
#bglb = Label(root, image = img)
#bglb.pack(fill=BOTH, expand=TRUE)


    var1=StringVar()
    var2=IntVar()
    radio_var=StringVar()
    cid1=StringVar(root,value='YYYY-MM-DD')
    cod1=StringVar(root,value='YYYY-MM-DD')
    # include check in and checkout inputs
#create image
    canvas=Canvas(root,width=300,height=300)
    canvas.pack(fill=BOTH, expand=TRUE)
    img = PhotoImage(file="room.png")
    canvas.create_image(0,0,image=img, anchor=NW)

#branch=droplist
#if we want any object of ttk to run then use ttk explicitely
    lab1=Label(root,text="Branch : " ,fg="black",font=("comic sans",10,"bold" ))
    lab1.place(x=110,y=120)
    list=["Mumbai","New Delhi","Chennai","Kolkata"]
    droplist=OptionMenu(root,var1,*list)
    var1.set("Select the branch")
    droplist.configure(width=20)
    droplist.place(x=220,y=120)
#room type = droplist
    lab2=Label(root,text="Room type  : " ,fg="black",bg="#e6edf5",font=("comic sans",10,"bold" ))
    lab2.place(x=110,y=160)
    list2=[ '1','2','3']
    droplist2=OptionMenu(root,var2,*list2)
    var2.set("Number of beds")
    droplist2.configure(width=20)
    droplist2.place(x=220,y=160)
#roomview=radio button
    lab3=Label(root,text="Room View  : " ,fg="black",bg="#e6edf5",font=("comic sans",10,"bold" ))
    lab3.place(x=110,y=200)
    r1=Radiobutton(root,text="Yes",variable=radio_var,value="true").place(x=230,y=200)
    r2=Radiobutton(root,text="No",variable=radio_var,value="false").place(x=320,y=200)
#check in dates
    lab4=Label(root,text="Check in :",fg="black",bg="#e6edf5",font=("comic sans",10,"bold" ))
    lab4.place(x=110,y=240)

    indate = Entry(root, textvar=cid1).place(x=220, y=240)
    lab5=Label(root,text="Check out :",fg="black",bg="#e6edf5",font=("comic sans",10,"bold" ))
    lab5.place(x=110,y=280)
    outdate = Entry(root, textvar=cod1).place(x=220, y=280)
    s1=ttk.Style()
    s1.configure('W.TButton', font =('calibri', 20, 'bold', 'underline'),
                foreground = 'Black',background='grey')
    c2=ttk.Button(root,text="CHECK",style="W.TButton",command=check_availabilty).place(x=400,y=330)   #
    root.mainloop()